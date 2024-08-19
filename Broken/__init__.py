import asyncio
import importlib
from pyrogram import Client
from config import (API_ID, API_HASH, SUDO_USERS, OWNER_ID, BOT_TOKEN,
                    STRING_SESSION1, STRING_SESSION2, STRING_SESSION3,
                    STRING_SESSION4, STRING_SESSION5, STRING_SESSION6,
                    STRING_SESSION7, STRING_SESSION8, STRING_SESSION9,
                    STRING_SESSION10)
from datetime import datetime
import time
from aiohttp import ClientSession

StartTime = time.time()
START_TIME = datetime.now()
CMD_HELP = {}
SUDO_USER = SUDO_USERS
clients = []
ids = []

SUDO_USERS.append(OWNER_ID)


if not BOT_TOKEN:
    print("⚠: BOT TOKEN NOT FOUND PLZ ADD ")
    
app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Broken/modules/bot"),
    in_memory=True,
)


async def initialize_clients():
    global aiosession
    aiosession = ClientSession()

    if API_ID:
        API_ID = API_ID
    else:
        print("WARNING: API ID NOT FOUND USING BROKEN API ⚠️")
        API_ID = "29700858"

    if API_HASH:
        API_HASH = API_HASH
    else:
        print("WARNING: API HASH NOT FOUND USING BROKEN API ⚠️")
        API_HASH = "2678024082871bdbf8c822e0fe63877c"

    
    for i in range(1, 11):
        session_string = globals().get(f"STRING_SESSION{i}")
        if session_string:
            print(f"Client{i}: Found.. Starting.. 📳")
            client = Client(
                name=f"client{i}",
                api_id=API_ID,
                api_hash=API_HASH,
                session_string=session_string,
                plugins=dict(root="Broken/modules")
            )
            clients.append(client)

async def main():
    await initialize_clients()
    
    await app.start()
    await asyncio.gather(*[client.start() for client in clients])

if __name__ == "__main__":
    asyncio.run(main())
