# For @UniBorg

# Courtesy @yasirsiddiqui

"""

.bye

"""


import time

from telethon.tl.functions.channels import LeaveChannelRequest

from telebot.utils import admin_cmd


@telebot.on(admin_cmd(pattern="bye", outgoing=True))
async def leave(e):

    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):

        await e.edit("`People here are so dumb 😑. I'm leaving.`")

        time.sleep(3)

        if "-" in str(e.chat_id):

            await borg(LeaveChannelRequest(e.chat_id))

        else:

            await e.edit("`This is Not A Chat. Please use this in groups :/`")
