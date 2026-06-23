# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from pyrogram import Client
from config import BOT_TOKEN, API_ID, API_HASH
from keep_alive import keep_alive
import threading
import time

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
    # Keep Alive ကို စတင်မယ်
    keep_alive()
    
    print("Bot Started")
    
    # Webhook ကို သတ်မှတ်မယ် (Pyrogram အတွက်)
    # ဒါပေမယ့် Pyrogram က Webhook ကို မပံ့ပိုးတာမို့ Long Polling ကိုပဲ သုံးမယ်
    app.run()

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
