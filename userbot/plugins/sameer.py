#credits to @Lodu_lalit#beautification credits to @sensei_nex for @LEGENDX22

#IMG CREDITS: @WhySooSerious
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins

# uptime = get_readable_time((time.time() - Lastupdate))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/63d4d2db589431ca8efdb.jpg"
pm_caption = "SBKA BAAP SAMEER\n\n"

@borg.on(admin_cmd(pattern=r"sameer"))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .sexxy command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()

    
@borg.on(admin_cmd(pattern=r"sameer", allow_sudo=True))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
