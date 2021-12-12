# Telegram QTMU bot
Source for [@QTMUbot](https://t.me/qtmubot) on Telegram.

QTMU stands for **Quick Telegraph Media Upload**, which this bot does.
It just uploads any .png, .jpg, .gif or .mp4 to Telegraph so your media could have convenient link.

## How it works
Telethon library creates a bot instance, waiting for media files. When it recieves one - downloads it into `./downloaded`, and then uploads it straight into Telegraph, returning a link to your media. Simple and quick! 

## Requirements
 * Python 3.7+
 * [Telethon 1.23.0+](https://github.com/LonamiWebs/Telethon)
 * [telegraph-api](https://github.com/python273/telegraph)
 * Telegram API codes, get one using [this tutorial](https://core.telegram.org/api/obtaining_api_id)

## How to start
You can either use [@QTMUbot](https://t.me/qtmubot) or host your own bot! 
To host your own bot:
 1. Get your TG API keys
 2. Create a new Telegram bot using [@botfather](https://t.me/botfather) and get the Bot API key
 3. Clone the repo 
 4. Change `api_id`, `api_hash` and `bot_token` with your credentials
    - You may also use different account name for Telegraph, [here](https://github.com/MrSnowball-dev/tg-qtmu-bot/blob/317a2debd244d87ba8aad7bb5f6664968c19d591/bot.py#L27)
 5. Use `python3 bot.py` to launch the bot
 6. Access the bot on Telegram, send media and get your Telegraph links! Also it works when you send something using other bot's inline requests (@gif, @pic etc.)
