import os
import time 
print("WELCOME THERE✨❣️✨")
time.sleep(1)
print("THIS IS ONLINE STRING_SESSION GENERATOR")

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

s = """
╔═══╦═══╦════╦═══╦═══╗
║╔═╗║╔═╗║╔╗╔╗║╔═╗║╔═╗║
║║─║║╚══╬╝║║╚╣╚═╝║║─║║
║╚═╝╠══╗║─║║─║╔╗╔╣║─║║
║╔═╗║╚═╝║─║║─║║║╚╣╚═╝║
╚╝─╚╩═══╝─╚╝─╚╝╚═╩═══╝

 ~ ASTRO UserBot
 
"""
print(s)
print("")

APP_ID = int(input("Enter API ID here: "))
API_HASH = input("Enter API HASH here: ")
with TelegramClient(
    StringSession(),
    APP_ID,
    API_HASH
  )as siya:
    print("")
    print("Below is your STRING_SESSION")
    print("")
    print(siya.session.save())
    print("")
    print("You can't copy This from here..GO TO YOUR SAVED MESSAGE TO COPY\nIT Can BE FOUND THERE😊")
    siya = siya.send_message("me", f"`{siya.session.save()}`")
    siya.reply("The Above is the your `STRING_SESSION` FOR your **AstroUB**\nFor any kind of Help Join ~ @Astro_HelpChat")