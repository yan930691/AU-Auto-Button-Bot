# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from pyrogram import Client

from config import (
    BOT_TOKEN,
    API_ID,
    API_HASH
)

from keep_alive import keep_alive

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

app = Client(
    "AU_AutoButtonBot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH,
    plugins={
        "root": "plugins"
    }
)

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

if __name__ == "__main__":

    keep_alive()

    print(
        "Bot Started"
    )

    app.run()

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
