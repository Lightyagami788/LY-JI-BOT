# For Astro-UB 
# OPEN CMD_LIST 

import os

from astro import CMD_HELP, CMD_HNDLR, CMD_LIST
from astro.config import Config

NAME = Config.NAME

DEFAULTUSER = str(NAME) if NAME else "Astro User✨"
CMD_HNDLR = Config.HNDLR
CUSTOM_HELP_EMOJI = os.environ.get("CUSTOM_HELP_EMOJI", "✨")

if CMD_HNDLR is None:
    CMD_HNDLR = "."


@astro.on(admin_cmd(pattern="help ?(.*)"))
async def cmd_list(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        tgbotusername = Config.BOT_USERNAME
        input_str = event.pattern_match.group(1)
        if tgbotusername is None or input_str == "text":
            string = ""
            for i in CMD_HELP:
                string += CUSTOM_HELP_EMOJI + " " + i + " " + CUSTOM_HELP_EMOJI + "\n"
                for iter_list in CMD_HELP[i]:
                    string += "    `" + str(iter_list) + "`"
                    string += "\n"
                string += "\n"
            if len(string) > 4095:
                with io.BytesIO(str.encode(string)) as out_file:
                    out_file.name = "cmd.txt"
                    await tgbot.send_file(
                        event.chat_id,
                        out_file,
                        force_document=True,
                        allow_cache=False,
                        caption="𝘾𝙊𝙈𝙈𝘼𝙉𝘿𝙎",
                        reply_to=reply_to_id,
                    )
                    await event.delete()
            else:
                await event.edit(string)
        elif input_str:
            if input_str in CMD_LIST:
                string = "**ƇƠMMƛƝƊƧ  ƛƔƛƖԼƛƁԼЄ Ɩn  {}** \n\n".format(input_str)
                if input_str in CMD_HELP:
                    for i in CMD_HELP[input_str]:
                        string += i
                    string += "\n\n**© @Astro_HelpChat**™"
                    await event.edit(string)
                else:
                    for i in CMD_LIST[input_str]:
                        string += "    " + i
                        string += "\n"
                    string += "\n**© @Astro_HelpChat**™"
                    await event.edit(string)
            else:
                await event.edit(input_str + " is not in My Plugins list!")
        else:
            help_string = f"""Hellow {DEFAULTUSER} This is ƛsτʀ๏ нєłρ мєηυ All Commands Are Available here..\nReport at [Astro_HelpChat](https://t.me/Astro_HelpChat) if any if them is **Not Working**"""
            try:
                results = await bot.inline_query(  # pylint:disable=E0602
                    tgbotusername, help_string
                )
                await results[0].click(
                    event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
                )
                await event.delete()
            except BaseException:
                await event.edit(
                    f"ӇЄԼԼƠ Ɩ ƛM ƝƠƬ ƛƁԼЄ ƬƠ ƦЄƔЄƛԼ ƛԼԼ ƇƠMMƛƝƊƧ ƁЄƇƛƲƧЄ MƳ ƖƝԼƖƝЄ ƖƧ ƊƖƧƛƁԼЄƊ 🤷🤦ƓЄƬ ӇЄԼƤ ƑƦƠM [Astro_HelpChat](https://t.me/Astro_HelpChat)", link_preview=False
                )
