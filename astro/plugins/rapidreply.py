import asyncio
import random
from astro import CMD_HELP
from astro.helps import memes as catmemes

que = {}


@bot.on(admin_cmd(incoming=True))
@bot.on(sudo_cmd(incoming=True, allow_sudo=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.3)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(catmemes.RRAID)),
            reply_to=event.message.id,
        )

@bot.on(admin_cmd(pattern="rapid(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="rapid(?: |$)(.*)", allow_sudo=True))
async def _(event):
    global que
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        b = await event.client.get_entity(a.sender_id)
        e = b.id
        c = b.first_name
        username = f"[{c}](tg://user?id={e})"
        event = await edit_or_reply(event, "Reply Raid Activating....")
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"Reply Raid has been activated on {username}")
    else:
        user = event.pattern_match.group(1)
        event = await edit_or_reply(event, "Reply Raid Activating....")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        que[e] = []
        qeue = que.get(e)
        appendable = [e]
        qeue.append(appendable)
        await event.edit(f"Reply Raid has been activated on {username}")


@bot.on(admin_cmd(pattern="stoprapid(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="stoprapid(?: |$)(.*)", allow_sudo=True))
async def _(event):
    global que
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        a = await event.get_reply_message()
        b = await event.client.get_entity(a.sender_id)
        e = b.id
        c = b.first_name
        username = f"[{c}](tg://user?id={e})"
        event = await edit_or_reply(event, "Reply Raid De-activating....")
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"Reply Raid has been De-activated on {username}")
    else:
        user = event.pattern_match.group(1)
        event = await edit_or_reply(event, "Reply Raid De-activating....")
        a = await event.client.get_entity(user)
        e = a.id
        c = a.first_name
        username = f"[{c}](tg://user?id={e})"
        queue = que.get(e)
        queue.pop(0)
        await event.edit(f"Reply Raid has been De-activated on {username}")


CMD_HELP.update(
    {
        "spam": "**Plugin : **`rapid`\
        \n\n**  •  Syntax : **`.rapid <username>`\
        \n**  •  Function : **__ Replies the user globally on every chat with random abuses. __\
        \n\n**  •  Syntax : **`.stoprapid <username>`\
        \n**  •  Function : **__ Deactivates the reply raid. __\
        \n\n\n**Note : Spam at your own risk !!**"
    }
)
