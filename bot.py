from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from telegraph import upload_file
from os import environ

API_ID = environ.get("API_ID")
API_HASH = environ.get("API_HASH")
BOT_TOKEN = environ.get("BOT_TOKEN")

app = Client(
  "Telegraph-Bot",
  api_id=API_ID,
  api_hash=API_HASH,
  bot_token=BOT_TOKEN
)

START_MSG = """Hᴀɪ {} 👋,
I Aᴍ Aɴ Pᴏᴡᴇʀꜰᴜʟ Tᴇʟᴇɢʀᴀᴩʜ Iᴍᴀɢᴇ Uᴩʟᴏᴀᴅᴇʀ Bᴏᴛ. Sᴇɴᴛ Mᴇ Aɴ Iᴍᴀɢᴇ Uɴᴅᴇʀ 5 Mʙ I Wɪʟʟ Cᴏɴᴠᴇʀᴛ Iᴛ Tᴏ Tᴇʟɢʀᴀ.ᴩʜ Lɪɴᴋ.
Tʜɪꜱ Bᴏᴛ Iꜱ Mᴀᴅᴇ Bʏ @ZiB_BoTs💞"""
