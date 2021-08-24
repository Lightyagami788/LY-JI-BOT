# Astro-UB # 

from astro.plugins.assistant.sql.blacklist_sql import all_bl_users
from astro.plugins.assistant.sql.userbase_sql import full_userbase
from telethon import events
from astro.plugins import OWNER_ID


@tgbot.on(events.NewMessage(pattern="^/stats", from_users=OWNER_ID))
async def tele(event):
    allu = len(full_userbase())
    blu = len(all_bl_users())
    await tgbot.send_message(event.chat_id,
                             "Here is the stats for your bot:\nTotal Users = {}\nBlacklisted Users = {}".format(allu, blu)
                             )
