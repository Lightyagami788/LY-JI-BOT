import time
from datetime import datetime
from io import BytesIO
import requests
from astro.plugins import PYTHON, OWNER_ID, ASTRO
from astro import bot, vision, StartTime
from astro import CMD_HELP 
from astro.utils import admin_cmd, sudo_cmd
from astro.config import Config 
from telethon.errors import ChatSendInlineForbiddenError as king
from telethon.errors.rpcerrorlist import BotMethodInvalidError as barsh

# Configs #
botname = Config.BOT_USERNAME
NAME = Config.NAME
A_PIC = Config.A_PIC if Config.A_PIC else "https://telegra.ph/file/bc41c5a01e076dfc15293.mp4"
A_TEXT = Config.A_TEXT if Config.A_TEXT else " This is ƛsτʀ๏\n   Ready in your protection"
emoji = "**❅**" 
emoji2 = "༺"
emoji3 = "༻"

# This is 4 later Purpose # 

if Config.SUDO_USERS:
    sudo = "Enabled"
else:
    sudo = "Disabled"
# uptime 
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
              remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
      
    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time
 
start = datetime.now()
myid = bot.uid
    # By @Alone_loverBoy
end = datetime.now()
(end - start).microseconds / 1000
uptime = get_readable_time((time.time() - StartTime))

MYUSER = f"[{ASTRO}](tg://user?id={OWNER_ID})"
astro = f"**『• Welcome To ƛsτʀ๏ •』**\n\n"
astro += f"**{A_TEXT}**\n\n"
astro += f"{emoji2}**iɲƒ๏ σƒ ƛsτʀ๏**{emoji3}\n"
astro += f"{emoji}** ƛsτʀ๏  Vision** ⊳≫ `{vision}`\n"
astro += f"{emoji}** Python Vision** ⊳≫  `{PYTHON}`\n"
astro += f"{emoji}** ƛsτʀ๏ uptime** ⊳≫ `{uptime}`\n"
astro += f"{emoji}** SUDO USER** ⊳≫ `{sudo}`\n"

astro += f"{emoji}** мy мαsтєя** ⊳≫ {MYUSER}\n\n"
astro += f"༆**✨Repository✨** ⊳≫ [GITHUB Repository✨](https://github.com/AstroUB/AstroUB)"

@bot.on(admin_cmd(pattern="alive"))
@bot.on(sudo_cmd(pattern="alive", allow_sudo=True))
async def amireallyalive(alive):
    try:
        astro = await bot.inline_query(botname, "alive")
        await astro[0].click(alive.chat_id)
        if alive.sender_id == bot.uid:
            await alive.delete()
    except (king, barsh):
        await eor(alive, caption=astro)
    
CMD_HELP.update({"alive": "→ `.alive`\nUse - Check if your bot is working."})
 
# ASTRO-UserBot
# © @Alone_loverboy
