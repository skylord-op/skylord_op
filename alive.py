import os
import asyncio
import random
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME, ALIVE_PIC
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "SKYLORD USERBOT"

SKYLORD_PIC="https://telegra.ph/file/3f79ca923137a181ab4c3.jpg"

if ALIVE_PIC is None:
    ALIVE_PIC=SKYLORD_PIC

    ALIVE_PIC=ALIVE_PIC

pm_caption = "**MR IZ SKYLORD 🇺🇸🇪🇷🇧o🇹**\n"
pm_caption += f"**My Master** => **{DEFAULTUSER}**\n\n"
pm_caption += f"**{DEFAULTUSER} i am  alive 😁😁😋😋**\n\n"
pm_caption +=f"**JUST CHILL AND DO WHATEVER YOU WANT TO DO WITH ME😉**\n\n"
pm_caption +=f"**Python Version => 3.9.1**\n\n"
pm_caption +=f"**Telethon Version => 1.15.0**\n\n"
pm_caption +=f"**[Support Group](https://t.me/skylord_help_chat)**\n\n"
pm_caption +=f"**[Channel for Updates](https://t.me/skylord_userbot_channel)**\n\n"
pm_caption +=f"**[owner of SKYLORD ](https://t.me/koi_nhi_apna)**\n\n"
pm_caption += "[REPO IS HERE](https://github.com/skylord-op/skylord_op)**\n\n"
pm_caption +=("  ______   ___  ____  ____  ____  _____       ___   _______     ______    \n"
              ".' ____ \ |_  ||_  _||_  _||_  _||_   _|    .'   `.|_   __ \   |_   _ `.  \n"
              "| (___ \_|  | |_/ /    \ \  / /    | |     /  .-.  \ | |__) |    | | `. \\n"
              " _.____`.   |  __'.     \ \/ /     | |   _ | |   | | |  __ /     | |  | | \n"
              "| \____) | _| |  \ \_   _|  |_    _| |__/ |\  `-'  /_| |  \ \_  _| |_.' / \n"
              " \______.'|____||____| |______|  |________| `.___.'|____| |___||______.'  \n"
              "                                                                         \n")
@borg.on(admin_cmd(pattern=r"SKYLORD IS ALIVE......"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id,file=ALIVE_PIC,caption=pm_caption)
    await alive.delete()
