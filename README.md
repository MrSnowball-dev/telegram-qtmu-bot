# Telegram QTMU bot
Source for [@QTMUbot](https://t.me/qtmubot) on Telegram.

QTMU stands for **Quick Telegraph Media Upload**, which this bot does.
It just uploads any .png, .jpg, .gif or .mp4 to Telegraph so your media could have convenient link.

## How it works:
Telethon library creates a bot instance, waiting for media files. When it recieves one - downloads it into `./downloaded`, and then uploads it straight into Telegraph, returning a link to your media. Simple and quick! 

## Requirements:
 * [Telethon >=1.23.0](https://github.com/LonamiWebs/Telethon)
 * [telegraph-api](https://github.com/python273/telegraph)
 * Telegram API codes, get one using [this tutorial](https://core.telegram.org/api/obtaining_api_id)
