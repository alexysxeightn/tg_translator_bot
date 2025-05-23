# Telegram Translator Bot

This bot uses AI to translate text between languages using OpenAI's API.

![gif](https://drive.google.com/uc?export=view&id=1anlhQG-80pHvH_iXAEbvqOufglL3zvcM)

## Setup

1. Clone the repo.

```
git clone https://github.com/alexysxeightn/tg_translator_bot.git
cd tg_translator_bot
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Create `.env` file with your Telegram and OpenAI tokens

```
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
OPENAI_API_KEY=your_openai_api_key
```

4. Run the bot

```
python -m bot.main
```

## Project structure

```
├── bot/
│   ├── __init__.py
│   ├── main.py
│   ├── handlers.py
│   ├── keyboards.py
│   └── translate.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── .env
├── requirements.txt
└── README.md
```
