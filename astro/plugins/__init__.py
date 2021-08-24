from astro.config import Config 
from astro import bot 
from astro import vision 
NAME = Config.NAME
OWNER_ID = Config.OWNER_ID
BOT_USERNAME = Config.BOT_USERNAME
OWNER_USERNAME = Config.OWNER_USERNAME
ASTRO = "@Astro_UserBot"
# Oh Yes...
if Config.SUDO_USERS:
    sudo = "YES Have Sudo"
else:
    sudo = "Nope No Sudo"
if Config.PMSECURITY.lower() == "off":
    pm = "DE-ACTIVE"
else:
    pm = "ACTIVE"

astro = f"ƛsτʀ๏ Vision: {vision}\n"
astro += f"SUDO USERS: {sudo}\n"
astro += f"PM SECURITY: {pm}\n"
astro += f"Assistant: {BOT_USERNAME}\n"
astro += f"My Master: {OWNER_USERNAME}\n"
astro += f"Protected by: {ASTRO}\n\n"

astrostats = f"{astro}"


# FOR PING LITTLE SETUP 
ASTRO = bot.me.first_name
OWNER_ID = bot.me.id
NAAME = str(NAME) if NAME else "Astro User✨"

masteri = "𝐁𝐄𝐋𝐎𝐖 𝐈𝐒 𝐀𝐁𝐎𝐔𝐓 𝐌𝐘 𝐌𝐀𝐒𝐓𝐄𝐑🥷\n\n"
masteri += f"USERNAME: {OWNER_USERNAME}\n"
masteri += f"ID: {OWNER_ID}\n"
masteri += f"NAME: {NAAME}\n"
masteri += "IS BOT: False\n"
masteri += f"Assistant: {BOT_USERNAME}\n\n"
masterinfo = f"{masteri}"

testro = "Hello This is About me😚\n"
testro += "Name: ƛsτʀ๏ υsєяъ๏т\n"
testro += f"Vision: {vision}\n"
testro += "Maintained🤔: Yes\n"
testro += "Gives Security: OP level\n"
testro += "Creator: @Alone_loverboy\n\n"

aboutastro = f"{testro}"
# PYTHON VISION 
PYTHON = "3.9.6"
