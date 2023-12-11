import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "Zaid"])

async def join(client):
    try:
        await client.join_chat("RONNY_KI_DUNIYA")
    except BaseException:
        pass
