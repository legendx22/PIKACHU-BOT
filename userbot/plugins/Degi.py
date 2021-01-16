"""Fun pligon...for HardcoreUserbot
\nCode by @Rambo_86
type `.degi` and `.nehi` to see the fun.
"""
import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="degi ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("𝐖𝐎")
        await asyncio.sleep(0.7)
        await event.edit("𝐃𝐄𝐆𝐈")
        await asyncio.sleep(1)
        await event.edit("𝐓𝐔𝐌")
        await asyncio.sleep(0.8)
        await event.edit("𝐄𝐊𝐁𝐀𝐀𝐑")
        await asyncio.sleep(0.9)
        await event.edit("𝐌𝐀𝐍𝐆")
        await asyncio.sleep(1)
        await event.edit("𝐊𝐀𝐑")
        await asyncio.sleep(0.8)
        await event.edit("𝐓𝐎𝐇")
        await asyncio.sleep(0.7)
        await event.edit("𝐃𝐄𝐊𝐇 𝐍 𝐁𝐒𝐃𝐊 𝐖𝐀𝐋𝐀")
        await asyncio.sleep(1)
        await event.edit("`𝐖𝐎 𝐃𝐄𝐆𝐈 𝐓𝐔𝐌 𝐄𝐊 𝐁𝐀𝐀𝐑 𝐌𝐀𝐍𝐆 𝐊 𝐃𝐄𝐊𝐇𝐎 𝐍 𝐃𝐄𝐓𝐎 𝐏𝐀𝐊𝐀𝐃 𝐊 𝐏𝐄𝐋 𝐃𝐎 😫😫`")

@borg.on(events.NewMessage(pattern=r"\.nehi", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("`𝐅𝐈𝐑 𝐁𝐇𝐈 𝐍 𝐃𝐄 𝐓𝐎 𝐔𝐒𝐊𝐈 𝐁𝐄𝐇𝐍 𝐊𝐎 𝐏𝐀𝐊𝐀𝐃 𝐊𝐄 𝐏𝐄𝐋𝐎 𝐎 𝐉𝐀𝐑𝐔𝐑 𝐃𝐄𝐆𝐈 🤣🤣`")
    await asyncio.sleep(999)
