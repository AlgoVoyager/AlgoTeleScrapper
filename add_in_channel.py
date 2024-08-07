from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, UserNotMutualContactError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
import csv
import traceback
import time
import random
import os

# Account details
api_id = 20460228
api_hash = ''
phone = '+91'

session_name = ''

client = TelegramClient(str(session_name), api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    try:
        client.send_code_request(phone)
        client.sign_in(phone, input('Enter the code: '))
    except Exception as e:
        print("Error SignIn : ",e)
        exit()

def add_members():
    # List all CSV files in the current directory
    csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]
    print("Available CSV files:")
    for i, file in enumerate(csv_files, start=1):
        print(f"{i}. {file}")

    # Prompt user to select the input CSV file
    while True:
        try:
            file_choice = int(input("Enter the number of the CSV file you want to use: "))
            if 1 <= file_choice <= len(csv_files):
                input_file = csv_files[file_choice - 1]
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Prompt user to enter the target group or channel username
    channel_username = input("Enter the target group/channel username: ")

    # Read users from the selected CSV file
    users = []
    with open(input_file, encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=",", lineterminator="\n")
        next(rows, None)
        for row in rows:
            user = {}
            user['srno'] = row[0]
            user['username'] = row[1]
            user['id'] = int(row[2])
            user['name'] = row[4]
            users.append(user)

    # Ask if user wants to add all members or a specific range
    add_all = input("Do you want to add all members? (yes/no): ").strip().lower()

    if add_all == 'yes':
        startfrom = 1
        endto = len(users)
    else:
        startfrom = int(input("Start From (sr. no.) = "))
        endto = int(input("End To (sr. no.) = "))

    n = 0

    for user in users:
        if (int(startfrom) <= int(user['srno'])) and (int(user['srno']) <= int(endto)):
            n += 1
            if n % 50 == 0:
                time.sleep(900)  # Sleep for 15 minutes after every 50 members added
                quit()
            try:
                print(f"Adding {user['id']} - {user['username']}")

                if user['username'] == "":
                    print("No username, moving to next")
                    continue

                client(InviteToChannelRequest(
                    channel_username,
                    [user['username']]
                ))

                print("Waiting for 20-50 seconds...")
                time.sleep(random.randrange(20, 50))
            except PeerFloodError:
                print("Getting Flood Error from Telegram. Script is stopping now. Please try again after some time.")
                quit()
            except UserPrivacyRestrictedError:
                print("The user's privacy settings do not allow you to do this. Skipping.")
            except UserNotMutualContactError:
                print("The provided user is not a mutual contact. Skipping.")
            except:
                traceback.print_exc()
                print("Unexpected Error")
                continue
        elif int(user['srno']) > int(endto):
            print("Members added successfully")
            break

while True:
    add_members()
    again = input("Do you want to add members to another group/channel? (yes/no): ").strip().lower()
    if again != 'yes':
        break

client.disconnect()

# Programmed by @Pandu_21 #TG