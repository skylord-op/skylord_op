import asyncio

from userbot.plugins.sql_helper.mute_sql import is_muted, mute, unmute
from userbot.utils import admin_cmd


# @command(outgoing=True, pattern=r"^.gmute ?(\d+)?")
@borg.on(admin_cmd(pattern=r"gmute ?(\d+)?"))
async def startgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("U CANT MESS UP WITH MY MASTER --SKYLORD IZZ HERE........!!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit(
            "Please reply to a user or add their into the command to gmute them."
        )
    event.chat_id
    await event.get_chat()
    if is_muted(userid, "gmute"):
        return await event.edit("This user is already gmuted")
    try:
        mute(userid, "gmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit("U CANT MESS UP WITH MY MASTER --SKYLORD IZZ HERE........")


# @command(outgoing=True, pattern=r"^.ungmute ?(\d+)?")
@borg.on(admin_cmd(pattern=r"ungmute ?(\d+)?"))
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit(
            "SKYLORD FELLING PITY ON U....\n\n       SON TOLD SORRY.....LAST CHANCE DUDE "
        )
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit(
            "Please reply to a user......."
        )
    event.chat_id
    if not is_muted(userid, "gmute"):
        return await event.edit("This user is not gmuted")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit("SKYLORD FORGIVED U....... TELL SORRY")


@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()
