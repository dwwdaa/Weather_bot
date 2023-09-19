# Telegram Weather Bot Readme

## Introduction

Welcome to the Telegram Weather Bot! This bot is designed to provide weather information for a given location right within your Telegram chats. With this bot, you can easily check the current weather conditions, the forecast for the next few days, and more.

## Table of Contents

1. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
2. [Usage](#usage)
   - [Commands](#commands)
   - [Examples](#examples)
3. [Bot Features](#bot-features)
4. [Contributing](#contributing)

## Getting Started

### Prerequisites

Before you can use the Telegram Weather Bot, make sure you have the following:

1. A Telegram account.
2. Access to the Telegram platform (via a mobile app or web browser).
3. A token for the Telegram Bot API, which you can obtain by creating a bot on [BotFather](https://core.telegram.org/bots#botfather).
4. A token for the OWM API, which you can obtain from official web-site of [openweathermap](https://openweathermap.org/api).

### Installation

1. Clone this repository to your local machine or server:

   ```bash
   git clone https://github.com/Gammik/Weather_bot.git
   ```

2. Install the required dependencies. You might want to create a virtual environment to manage them:

   ```bash
   cd telegram-weather-bot
   pip install telebot
   pip install pyowm
   ```

3. Configure the bot by editing the `bot.py` file. Add your Telegram Bot API token obtained from BotFather and API token obtained from OWM.

4. Start the bot:

   ```bash
   python bot.py
   ```

Now, your Telegram Weather Bot should be up and running!

## Usage

### Commands

The Telegram Weather Bot responds to specific commands. Here are some of the main commands you can use:

- `/start`: Start the bot and get a welcome message.
- `/help`: Display the list of available commands and a brief explanation of how to use the bot.

### Examples

- To get the current weather for New York City, you can send the following message:

  ```
  New York City
  ```
- You don't need any command

## Bot Features

The Telegram Weather Bot provides the following features:

- Current weather information for a given location and advices.
- User-friendly commands and responses.

## Contributing

Contributions to this project are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test them thoroughly.
4. Create a pull request with a clear description of your changes.

---

Enjoy using the Telegram Weather Bot! If you have any questions or encounter issues, feel free to open an issue on GitHub or contact the bot's maintainers.
