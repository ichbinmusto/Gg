import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Broken"])

async def join(client):
    try:
        await client.join_chat("brokenxNetwork")
    except BaseException:
        pass
