import time 
from datetime import datetime 
from astro import bot
from astro.plugins import ASTRO, OWNER_ID
from astro.config import Config 
### Config ### 
 

@astro.on(admin_cmd(pattern=r"ping$"))
@astro.on(sudo_cmd(pattern=r"ping$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    event = await edit_or_reply(event, "β’ππππβ’")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f"""
βββββ
βββββ
βββββ βββ¦ββββββ
βββββ£ββββββ£βββ
ββββββββββββββ
ββββββββ©βββ©βββ
ββββββββββββββ
ββββββββββββββ
βε½‘ΖsΟΚΰΉ sΡΡΡ΅Δ±cΡ is ONε½‘β

βββΠΌαΊ ΠΌαΉ© β£ `{ms}s` β β \n
|β ΚΚ ΟΟΞ·ΡΡβ’ [{ASTRO}](tg://user?id={OWNER_ID}) β|
 \n
 ~ ΖsΟΚΰΉ ΟsΡΡΡΰΉΡ ~
""")
# Β© @Alone_loverboy 
# FOR OWN ASTRO UserBot
