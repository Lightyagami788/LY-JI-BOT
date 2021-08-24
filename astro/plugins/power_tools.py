"""Restart or Terminate the bot from any chat
Available Commands:
.restart
.shutdown"""

import os
import sys
import asyncio
from astro import CMD_HELP, CMD_HNDLR
from astro.utils import admin_cmd


@astro.on(admin_cmd(pattern="restart"))
async def _(event):
    if event.fwd_from:
        return
    await asyncio.sleep(2)
    await event.edit("Restarting \n□□□□□□□□□□")
    await asyncio.sleep(2)
    await event.edit(f"Restarting \n■■■■□□□□□□  ")
    await asyncio.sleep(2)
    await event.edit(f"Restarting \n■■■■■■■■□□   ")
    await asyncio.sleep(2)
    await event.edit(f"Done! \n■■■■■■■■■■  ")
    await asyncio.sleep(2)
    await event.edit(
        f"__Astro is Restarting...__\nPlease give it **a minute or two** and then use `{CMD_HNDLR}alive`! "
     )
    await borg.disconnect()
    # https://archive.is/im3rt
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()


@astro.on(admin_cmd(pattern="shutdown"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit(
        "astro is turning off... Manually turn me on later, from heroku."
    )
    await borg.disconnect()


CMD_HELP.update(
    {
        "power_tools": ".restart\nUse - Restart the bot.\
        \n\n.shutdown\nUse - shutdown the bot."
    }
)
