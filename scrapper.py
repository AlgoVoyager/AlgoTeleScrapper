from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import os
import csv
import sys

# Account details
api_id = 17184020
api_hash = ''
phone = '+91'
session_name = ''  # This session_name is for scraper

client = TelegramClient(str(session_name), api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))

def get_groups_and_channels(client):
    dialogs = client(GetDialogsRequest(
        offset_date=None,
        offset_id=0,
        offset_peer=InputPeerEmpty(),
        limit=200,
        hash=0
    ))

    groups = []
    for chat in dialogs.chats:
        if hasattr(chat, 'megagroup') and chat.megagroup:
            groups.append(chat)
        elif hasattr(chat, 'broadcast') and chat.broadcast:
            groups.append(chat)

    return groups

def scrape_members(client, target_group):
    print(f'Scraping members from {target_group.title}...')

    all_participants = client.iter_participants(target_group)

    print('Saving in file...')
    try:
        filename = target_group.title.replace(" ", "_") + ".csv"
        with open(filename, "w", encoding='UTF-8') as f:
            writer = csv.writer(f, delimiter=",", lineterminator="\n")
            writer.writerow(['sr. no.', 'username', 'user id', 'name', 'status'])
            for i, user in enumerate(all_participants, start=1):
                username = user.username or ""
                first_name = user.first_name or ""
                last_name = user.last_name or ""
                name = (first_name + ' ' + last_name).strip()
                writer.writerow([i, username, user.id, name, target_group.title])

        print('Members scraped successfully.')
    except Exception as e:
        print("Scraping failed:", e)
        if os.path.exists(filename):
            os.remove(filename)

while True:
    groups = get_groups_and_channels(client)
    
    if not groups:
        print("No groups or channels available to scrape.")
        break

    print('Available groups and channels:')
    for i, group in enumerate(groups, start=1):
        print(f"{i}. {group.title}")

    while True:
        try:
            choice = int(input("Enter the number of the group/channel you want to scrape: "))
            if 1 <= choice <= len(groups):
                target_group = groups[choice - 1]
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    scrape_members(client, target_group)

    continue_scraping = input("Do you want to scrape another group/channel? (yes/no): ").strip().lower()
    if continue_scraping != 'yes':
        break

client.disconnect()

# Programmed by @Pandu_21 #TG
