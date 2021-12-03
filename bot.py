from telethon import TelegramClient, events
from telegraph.aio import Telegraph
import logging
import os
import glob
# import asyncio

from settings import *

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

def logger(func):
    def decorator(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            logging.error(err, exc_info=True)
    return decorator

bot = TelegramClient('qtmu', api_id, api_hash).start(bot_token=bot_token)

@bot.on(events.NewMessage(func=(lambda event: event.file)))
@logger
async def incoming_file(event):
    telegraph = Telegraph()
    await telegraph.create_account(short_name='qtmubot')

    path = await event.message.download_media('./downloaded/')
    if event.message.file.ext in ['.jpg', '.jpeg', '.png', '.gif', '.mp4']:
        response = await telegraph.upload_file(path)
        await event.respond(f"https://telegra.ph{response[0]['src']}")

        files = glob.glob('./downloaded/*')
        for file in files:
            try:
                os.remove(file)
            except PermissionError:
                pass
    else:
        await event.respond(f"Sorry, I only accept .JPG, .PNG, .GIF, .MP4 files.")

@bot.on(events.NewMessage(pattern='/start'))
@logger
async def start_handler(event):
    await event.respond("Just send me a media and I will give you a telegraph link for it.")

@bot.on(events.NewMessage(pattern='/help'))
@logger
async def start_handler(event):
    await event.respond('''
Just send me .JPG, .PNG, .GIF or .MP4 file and I will get you it's telegra.ph link.

Useful for quick getting a file link if you need to share something outside of Telegram. Or inside (by using a link preview in your formatting).
''')

def main():
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()
