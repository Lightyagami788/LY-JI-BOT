# Astro-UB

"""
   Heroku manager for your userbot
"""

import asyncio
import math
import os
from astro.config import Config
import heroku3
import requests

from astro import CMD_HELP, CMD_HNDLR

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME

@astro.on(admin_cmd(pattern=r"(set|get|del) Config (.*)", outgoing=True))
async def Configiable(Config):
    """
    Manage most of ConfigConfigs setting, set new Config, get current Config,
    or delete Config...
    """
    if HEROKU_APP_NAME is not None:
        app = Heroku.app(HEROKU_APP_NAME)
    else:
        return await edit_or_reply(
            Config, "`[HEROKU]:" "\nPlease setup your` **HEROKU_APP_NAME**"
        )
    exe = Config.pattern_match.group(1)
    heroku_Config = app.config()
    if exe == "get":
        toput = await edit_or_reply(Config, "`Getting information...`")
        await asyncio.sleep(1.0)
        try:
            Configiable = Config.pattern_match.group(2).split()[0]
            if Configiable in heroku_Config:
                return await toput.edit(
                    "**ConfigConfigs**:" f"\n\n`{Configiable} = {heroku_Config[Configiable]}`\n"
                )
            return await toput.edit(
                "**ConfigConfigs**:" f"\n\n`Error:\n-> {Configiable} don't exists`"
            )
        except IndexError:
            configs = prettyjson(heroku_Config.to_dict(), indent=2)
            with open("configs.json", "w") as fp:
                fp.write(configs)
            with open("configs.json", "r") as fp:
                result = fp.read()
                if len(result) >= 4096:
                    await bot.send_file(
                        Config.chat_id,
                        "configs.json",
                        reply_to=Config.id,
                        caption="`Output too large, sending it as a file`",
                    )
                else:
                    await toput.edit(
                        "`[HEROKU]` ConfigConfigs:\n\n"
                        "================================"
                        f"\n```{result}```\n"
                        "================================"
                    )
            os.remove("configs.json")
            return
    elif exe == "set":
        Configiable = "".join(Config.text.split(maxsplit=2)[2:])
        toput = await edit_or_reply(Config, "`Setting information...`")
        if not Configiable:
            return await toput.edit("`.set Config <ConfigConfigs-name> <value>`")
        value = "".join(Configiable.split(maxsplit=1)[1:])
        Configiable = "".join(Configiable.split(maxsplit=1)[0])
        if not value:
            return await toput.edit(f"`{CMD_HNDLR}set Config <ConfigConfigs-name> <value>`")
        await asyncio.sleep(1.5)
        if Configiable in heroku_Config:
            await toput.edit(f"`{Configiable}` **successfully changed to **`{value}`")
        else:
            await toput.edit(
                f"`{Configiable}`** successfully added with value` **{value}`"
            )
        heroku_Config[Configiable] = value
    elif exe == "del":
        toput = await edit_or_reply(Config, "`Getting information to delete Configiable...`")
        try:
            Configiable = Config.pattern_match.group(2).split()[0]
        except IndexError:
            return await toput.edit("`Please specify ConfigConfigs you want to delete`")
        await asyncio.sleep(1.5)
        if Configiable in heroku_Config:
            await toput.edit(f"`{Configiable}` **has been successfully deleted**")
            del heroku_Config[Configiable]
        else:
            return await toput.edit(f"`{Configiable}`** doesn't exist**")


CMD_HELP.update(
    {
        "heroku": ".set Config <name> <value>\nUse - Set the Configiable with the value given.\
        \n\n.get Config <name>\ Get The Config"
    }
)
