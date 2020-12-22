#alive.py 
# animation Idea by hell user bot
# Made by @kraken_the_BadAss...
# Kang with credits else gay...
import asyncio
import random
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND BOT"

# op creation by @koi_nhi_apna

edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/70eea07a7a1944989c84d.mp4"
file2 = "https://telegra.ph/file/70eea07a7a1944989c84d.mp4"
file3 = "https://telegra.ph/file/59154a5d9c034091c64b8.jpg"
file4 = "https://telegra.ph/file/59154a5d9c034091c64b8.jpg"
""" =======================CONSTANTS====================== """
pm_caption = "⁪⁬⁮⁮⁮⁮ 𖣔ꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋ𖣔ꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋꠋ ‌VINCENZO✓ °•⋆⫷𝗕M̸B̸L̸𝗕⫸⋆•°✺꠵ࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧࣧ』 ɨֆ օռʟɨռɛ..!! **🔥🔥\n\n"
pm_caption += "⚔️⚔️ *Yes Master, Am Alive And Systems Are Working Perfectly As It Should Be...*⚔️⚔️\n\n"
pm_caption += "༆༄☠︎︎About My System \n\n"
pm_caption += "🔥🔥 *ᴛᴇʟᴇᴛʜᴏɴ*🔥🔥 >>》 15.0.0\n"
pm_caption += "🚨🚨 *group*🚨🚨   >>》 [ʝօɨռ](https://t.me/skylord_help_chat)\n"
pm_caption += f"🔰🔰*ᴍᴀsᴛᴇʀ*🔰🔰  >>》 {DEFAULTUSER}\n"
pm_caption += "🌏🌏 *ᴄʀᴇᴀᴛᴏʀ*🌏🌏  >>》 [ᴏᴡɴᴇʀ](https://t.me/koi_nhi_apna)\n\n"
pm_caption += "🔶🔶 *ᴄʀᴇᴅɪᴛs*🔶🔶  >>》 [ʙʀᴏ](https://t.me/hamaari_paltan)\n\n"
pm_caption += "[ ______   ___  ____  ____  ____  _____       ___   _______     ______\n' ____ \ |_  ||_  _||_  _||_  _||_   _|    .'   `.|_   __ \   |_   _ `.  \n| (___ \_|  | |_/ /    \ \  / /    | |     /  .-.  \ | |__) |    | | `. |\n_.____`.   |  __'.     \ \/ /     | |   _ | |   | | |  __ /     | |  | |\n| \____) | _| |  \ \_   _|  |_    _| |__/ |\  `-'  /_| |  \ \_  _| |_.' /\n\______.'|____||____| |______|  |________| `.___.'|____| |___||______.'\n](https://t.me/skylord_userbot_channel)\n\n"
@borg.on(admin_cmd(pattern=r"alive"))

async def amireallyalive(yes):
    chat = await yes.get_chat()

    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    await alive.delete()
    
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
