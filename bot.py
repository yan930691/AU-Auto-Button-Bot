# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from pyrogram import Client
from config import BOT_TOKEN, API_ID, API_HASH
from keep_alive import keep_alive, app as flask_app

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

# Pyrogram Client
bot = Client(
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
    # Keep Alive ကို စတင်မယ်
    keep_alive()
    
    print("Bot Started")
    
    # Pyrogram ကို Long Polling နဲ့ Run မယ်
    bot.run()

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
