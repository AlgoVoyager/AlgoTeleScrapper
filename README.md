# Telegram Scraper and Adder Bot

This repository contains a Python script for scraping members from Telegram groups or channels and adding them to another channel.

## Features

- Scrape members from Telegram groups or channels.
- Add scraped members to a specified Telegram channel.
- Supports selecting specific ranges of members to add.
- Handles exceptions and errors gracefully.

## Requirements

- Python 3.x
- `telethon` library

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **Generate API ID and Hash:**
   - Go to [my.telegram.org](https://my.telegram.org).
   - Log in with your phone number and enter the confirmation code sent to your Telegram app.
   - Navigate to the "API development tools" section.
   - Create a new application by providing the required details.
   - You will receive an API ID and an API hash.

2. **Edit the credentials:**
    - Open the `add_in_channel.py` file and update the following variables with your Telegram API credentials and phone number:
      ```python
      api_id = 'your_api_id'
      api_hash = 'your_api_hash'
      phone = 'your_phone_number'
      ```

3. **Prepare the input CSV file:**
    - Ensure you have a CSV file (`input_file.csv`) with the following columns: `sr. no.`, `username`, `user id`, `name`, `status`.
    - Place the CSV file in the same directory as the script or update the path in the script accordingly.

## Usage

1. **Run the script:**
    ```bash
    python add_in_channel.py
    ```

2. **Follow the prompts:**
    - Enter the code sent to your Telegram account.
    - Select the file to use for adding members.
    - Enter the target group or channel name.
    - Choose whether to add all members or specify a range.

## Notes

- Ensure that you have appropriate permissions to scrape members from the target group or channel.
- Respect Telegram's terms of service and privacy policies when using this script.
- Be cautious of rate limits and avoid sending too many requests in a short period.

## Troubleshooting

- **FloodWaitError:** If you encounter a `FloodWaitError`, it means that Telegram is rate-limiting your requests. Wait for the specified time before trying again.
- **UserNotMutualContactError:** This error occurs when the provided user is not a mutual contact. Ensure that the user has interacted with you or the bot before attempting to add them.
- **Other Errors:** If you encounter other errors, review the stack trace for more information and ensure that your credentials and input data are correct.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
