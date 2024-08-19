from Broken import app, API_ID, API_HASH
from config import OWNER_ID, ALIVE_PIC, SUDO_USERS
from pyrogram import filters
import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import * 

PHONE_NUMBER_TEXT = (
    "✘ Heya Do You Wanna Clone 👋!\n\n✘ I'm @MrBrokn Assistant \n\n‣ I can help you to host Just Ask My Master\n\n‣ This specially for Buzzy People's(lazy)\n\n‣ Now /clone {send your PyroGram String Session}"
)

@app.on_message(filters.command("start"))
async def hello(client: Client, message: Message):
    buttons = [
        [
            InlineKeyboardButton("✘ ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ", url="t.me/BrokenxNetwork"),
        ],
        [
            InlineKeyboardButton("✘ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url="t.me/+2tyYGwWgsb4zMWY1"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await client.send_photo(
        message.chat.id,
        ALIVE_PIC,   
        caption=PHONE_NUMBER_TEXT,   
        reply_markup=reply_markup
    )

@app.on_message(filters.user(SUDO_USERS + [OWNER_ID]) & filters.command("clone"))
async def clone(bot: app, msg: Message):
    chat = msg.chat
    text = await msg.reply("Usage:\n\n /clone session")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("Booting Your Client")
                   
        client = Client(name="Melody", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="Broken/modules"))
        await client.start()
        user = await client.get_me()
        await msg.reply(f"Your Client Has Been Successfully Started As {user.first_name} ✅.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
