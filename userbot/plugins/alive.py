#alive.py 
# Made by @koi_nhi_apna...
# use with credits or else u will get strike....
import asyncio
import random
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
# hehehehehe
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "SKYLORD BOT"

# creation by @koi_nhi_apna

edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/eae33338a14f99a3f9ec1.mp4"
file2 = "https://telegra.ph/file/eae33338a14f99a3f9ec1.mp4"
file3 = "https://telegra.ph/file/7de2b2f0de86dc19b0e96.jpg"
file4 = "https://telegra.ph/file/7de2b2f0de86dc19b0e96.jpg"
""" =======================CONSTANTS====================== """
pm_caption = "⁪⁬⁮⁮⁮⁮ HEYA SKYLORD ɨֆ օռʟɨռɛ..!! **🔥🔥\n\n"
pm_caption += "⚔️⚔️ *Yes Master, I Am Alive And Systems Are Working Perfectly.. Let's Rock Together...hehehehehe...*⚔️⚔️\n\n"
pm_caption += "༆༄☠︎︎About My System \n\n"
pm_caption += "🔥🔥 *ᴛᴇʟᴇᴛʜᴏɴ*🔥🔥 >>》 20.0.0\n"
pm_caption += "🚨🚨 *group*🚨🚨   >>》 [ʝօɨռ](https://t.me/skylord_help_chat)\n"
pm_caption += f"🔰🔰*ᴍᴀsᴛᴇʀ*🔰🔰  >>》 {DEFAULTUSER}\n"
pm_caption += "🌏🌏 *ᴄʀᴇᴀᴛᴏʀ*🌏🌏  >>》 [ᴏᴡɴᴇʀ](https://t.me/koi_nhi_apna)\n\n"
pm_caption += "🔶🔶 *channel*🔶🔶  >>》 [ʝօɨռ](https://t.me/skylord_userbot_channel)\n\n"
pm_caption += "*clan/gang* >>》 [         ,-.\n     ___,---.__          /'|`\          __,---,___/n,-'    \`    `-.____,-'  |  `-.____,-'    //    `-./n,'        |           ~'\     /`~           |        `./n /      ___//              `. ,'          ,  , \___      \/n|    ,-'   `-.__   _         |        ,    __,-'   `-.    |/n|   /          /\_  `   .    |    ,      _/\          \   |/n\  |           \ \`-.___ \   |   / ___,-'/ /           |  //n\  \           | `._   `\\  |  //'   _,' |           /  //n`-.\         /'  _ `---'' , . ``---' _  `\         /,-'/n``       /     \    ,='/ \`=.    /     \       ''/n |__   /|\_,--.,-.--,--._/|\   __|/n /  `./  \\`\ |  |  | /,//' \,'  \/n /   /     ||--+--|--+-/-|     \   \/n|   |     /'\_\_\ | /_/_/`\     |   |/n\   \__, \_     `~'     _/ .__/   //n `-._,-'   `-._______,-'   `-._,-'/n](https://t.me/BFA_CLAN)\n\n"
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
