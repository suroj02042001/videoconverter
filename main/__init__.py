#ChauhanMahesh/DroneBots/COL

from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
BOT_UN = config("BOT_UN", default=None)
#AUTH_USERS = config("AUTH_USERS", default=None)
#LOG_CHANNEL = config("LOG_CHANNEL", default=None, cast=int)
#ACCESS_CHANNEL = config("ACCESS_CHANNEL", default=None, cast=int)

Drone = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
