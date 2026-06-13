# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from pyrogram import Client, filters

from config import OWNER_ID
from database import (
    add_admin,
    remove_admin,
    get_admins
)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

def owner(_, __, msg):

    return (
        msg.from_user
        and msg.from_user.id == OWNER_ID
    )


owner_filter = filters.create(owner)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@Client.on_message(
    filters.command("addadmin")
    & owner_filter
)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def add_admin_cmd(
    client,
    message
):

    if len(message.command) < 2:

        return await message.reply_text(
            "Usage:\n/addadmin USER_ID"
        )


    uid = int(
        message.command[1]
    )

    await add_admin(uid)

    await message.reply_text(
        f"✅ Admin Added\n{uid}"
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@Client.on_message(
    filters.command("removeadmin")
    & owner_filter
)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def remove_admin_cmd(
    client,
    message
):

    if len(message.command) < 2:

        return await message.reply_text(
            "Usage:\n/removeadmin USER_ID"
        )


    uid = int(
        message.command[1]
    )

    await remove_admin(uid)


    await message.reply_text(
        f"✅ Admin Removed\n{uid}"
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

@Client.on_message(
    filters.command("admins")
    & owner_filter
)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def admins_cmd(
    client,
    message
):

    admins = await get_admins()


    if not admins:

        return await message.reply_text(
            "No admins"
        )


    text = "👮 Admins\n\n"

    for x in admins:

        text += f"• {x}\n"


    await message.reply_text(text)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
