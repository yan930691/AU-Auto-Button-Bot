# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from pyrogram import Client, filters
from config import OWNER_ID

# shared global variable
THUMBNAIL = None


@Client.on_message(
    filters.command("thumbnail") & filters.private
)
async def set_thumbnail(client, message):

    global THUMBNAIL

    if not message.from_user or message.from_user.id != OWNER_ID:
        return

    if not message.reply_to_message or not message.reply_to_message.photo:
        return await message.reply_text(
            "Reply to an image to set thumbnail."
        )

    # download and store local file path (IMPORTANT for video/document thumb)
    THUMBNAIL = await message.reply_to_message.download(
        file_name="thumb.jpg"
    )

    await message.reply_text("✅ Thumbnail saved")

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
