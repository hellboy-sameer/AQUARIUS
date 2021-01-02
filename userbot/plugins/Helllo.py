"""COMMAND : .helllo"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


@borg.on(admin_cmd("helllo"))
async def (event):
    if event.fwd_from:
        return
    mentions = "⁭
💖💖                        💖💖
💖💖                        💖💖
💖💖                        💖💖
💖💖                        💖💖
💖💖💖💖💖 💖💖💖
💖💖💖💖💖 💖💖💖
💖💖                        💖💖
💖💖                        💖💖
💖💖                        💖💖
💖💖                        💖💖
⁭
💟💟💟💟💟💟💟💟
💟💟💟💟💟💟💟💟
💟💟
💟💟
💟💟💟💟💟💟
💟💟💟💟💟💟
💟💟
💟💟
💟💟💟💟💟💟💟💟
💟💟💟💟💟💟💟💟
⁭
💟💟
💟💟
💟💟
💟💟
💟💟
💟💟
💟💟
💟💟
💟💟💟💟💟💟💟💟
💟💟💟💟💟💟💟💟
⁭
💟💟
💟💟
💟💟
💟💟
💟💟
💟💟
💟💟
💟💟
💟💟💟💟💟💟💟💟
💟💟💟💟💟💟💟💟
⁭
           💖💖💖💖💖
     💖💖💖💖💖💖💖
   💖💖                   💖💖
 💖💖                       💖💖
💖💖                         💖💖
💖💖                         💖💖
 💖💖                       💖💖
   💖💖                   💖💖
      💖💖💖💖💖💖💖
            💖💖💖💖💖"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
