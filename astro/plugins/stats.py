# Thanks to Lucifer #

import time

from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User

from astro import CMD_HELP
from astro.utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd(pattern="stats$"))
@bot.on(sudo_cmd(pattern="stats$", allow_sudo=True))
async def stats(
    event: NewMessage.Event,
) -> None:  # pylint: disable = R0912, R0914, R0915
    """Command to get stats about the account"""
    alain = await edit_or_reply(event, "`ωαιт ℓєммє cσllєcт уσυя ѕтαтѕ...`")
    start_time = time.time()
    private_chats = 0
    bots = 0
    groups = 0
    broadcast_channels = 0
    admin_in_groups = 0
    creator_in_groups = 0
    admin_in_broadcast_channels = 0
    creator_in_channels = 0
    unread_mentions = 0
    unread = 0
    dialog: Dialog
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel):
            # participants_count = (await event.get_participants(dialog,
            # limit=0)).total
            if entity.broadcast:
                broadcast_channels += 1
                if entity.creator or entity.admin_rights:
                    admin_in_broadcast_channels += 1
                if entity.creator:
                    creator_in_channels += 1
            elif entity.megagroup:
                groups += 1
                # if participants_count > largest_group_member_count:
                #     largest_group_member_count = participants_count
                if entity.creator or entity.admin_rights:
                    # if participants_count > largest_group_with_admin:
                    #     largest_group_with_admin = participants_count
                    admin_in_groups += 1
                if entity.creator:
                    creator_in_groups += 1
        elif isinstance(entity, User):
            private_chats += 1
            if entity.bot:
                bots += 1
        elif isinstance(entity, Chat):
            groups += 1
            if entity.creator or entity.admin_rights:
                admin_in_groups += 1
            if entity.creator:
                creator_in_groups += 1
        unread_mentions += dialog.unread_mentions_count
        unread += dialog.unread_count
    time.time() - start_time
    full_name = inline_mention(await event.client.get_me())
    response = f"**❣️ ѕтαтѕ σf {full_name} ❣️**\n**❅──────✧❅✦❅✧──────❅**\n"
    response += f"**❅** ✘ **ρяιναтє chαt:** `{private_chats}` ✘\n"
    response += f"**❅** ✘ **usєrs:** `{private_chats - bots}` ✘\n"
    response += f"**❅** ✘ **вσts:** `{bots}` ✘\n**❅──────✧❅✦❅✧──────❅**\n**❅──────✧❅✦❅✧──────❅**\n"
    response += f"**❅** ✘ **gяσυρ:** `{groups}` ✘\n"
    response += f"**❅** ✘ **crєαtσr:** `{creator_in_groups}` ✘\n"
    response += f"**❅** ✘ **α∂мנи:** `{admin_in_groups}` ✘ \n"
    response += f"**❅** ✘ **α∂мιи яιgнтs:** `{admin_in_groups - creator_in_groups}` ✘\n**❅──────✧❅✦❅✧──────❅**\n**❅──────✧❅✦❅✧──────❅**\n"
    response += f"**❅** ✘ **cнαииєℓ:** `{broadcast_channels}` ✘ \n"
    response += f"**❅** ✘ **cяєαтσя:** `{creator_in_channels}` ✘ \n"
    response += f"**❅** ✘ **α∂мιи:** `{admin_in_broadcast_channels}` ✘ \n"
    response += f"**❅** ✘ **α∂мנи яιgнтѕ:** `{admin_in_broadcast_channels - creator_in_channels}` ✘\n**❅──────✧❅✦❅✧──────❅**\n**❅──────✧❅✦❅✧──────❅**\n"
    response += f"**❅** ✘ **υияєα∂ мєѕѕαgє:** `{unread}` ✘\n"
    response += (
        f"**❅** ✘ **υияєα∂ мєитισиѕ:** `{unread_mentions}` ✘\n**❅──────✧❅✦❅✧──────❅**\n"
    )
    response += f"→ **Powered by [Astro-UB](t.me/Astro_HelpChat)** ←"
    await alain.edit(response)


def make_mention(user):
    if user.username:
        return f"@{user.username}"
    return inline_mention(user)


def inline_mention(user):
    full_name = user_full_name(user) or "No Name"
    return f"[{full_name}](tg://user?id={user.id})"


def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    return " ".join(names)


CMD_HELP.update(
    {
        "stat": "**Plugin : **`stats`\
    \n\n**Syntax : **`.stats`\
    \n**Function : **Shows you the count of  your groups, channels, private chats...etc"
    }
)
