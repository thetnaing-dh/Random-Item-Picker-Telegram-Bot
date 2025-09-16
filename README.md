# Random Item Picker Telegram Bot
A Python-based Telegram bot that randomly selects an item from a list provided by users. 
Users can add multiple items and when they send the "done" message, 
the bot will randomly pick and display one item from the list.

![CoverImage](https://github.com/thetnaing-dh/Random-Item-Picker-Telegram-Bot/blob/main/tele_bot.png?raw=true)

## Features
* Interactive conversation with the bot
* Collect multiple items from users
* Random selection algorithm
* Simple and intuitive interface

## Prerequisites
* Python 3.7+
* A Telegram Bot Token from BotFather
* python-telegram-bot library

## Installation
* Clone this repository:

      bash
      
      git clone https://github.com/your-username/random-item-picker-bot.git
      cd random-item-picker-bot
      
* Install the required dependencies:


      bash
      
      pip install python-telegram-bot

* Set up your environment variables:

      Copy .env.example to .env

* Add your Telegram Bot Token to the .env file:

      BOT_TOKEN=your_telegram_bot_token_here
  
## Usage
* Run the bot:

      bash
      python bot.py
  
* Start a conversation with your bot on Telegram
* Send the /start command to begin
* Enter your items one by one
* Send "done" when you've finished adding items
* The bot will randomly select and display one item from your list

## How It Works
* The bot uses the python-telegram-bot library to handle Telegram API interactions
* It maintains a conversation handler with two states:
  * Collecting items
  * Waiting for the "done" command
* When "done" is received, it uses Python's random module to select an item
* The selected item is sent back to the user

## File Structure

      random-item-picker-bot/
      ├── bot.py              # Main bot implementation
      ├── .env               # Environment variables (create this)
      ├── .env.example       # Example environment variables
      ├── requirements.txt   # Project dependencies
      └── README.md          # This file

## Contributing
* Fork the repository
* Create a feature branch
* Make your changes
* Submit a pull request

## License
This project is Open Source no need LICENSE file.

## Support
If you encounter any issues or have questions, please open an issue in the GitHub repository.
