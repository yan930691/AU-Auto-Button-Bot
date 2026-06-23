# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from flask import Flask, request
from threading import Thread

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

app = Flask(__name__)


@app.route("/")
def home():
    return "Bot Running"


# 🔥 Webhook Route ထည့်ထားတယ်
@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        # Telegram က လာတဲ့ Update ကို လက်ခံတယ်
        data = request.get_json(force=True)
        # ဒီနေရာမှာ Pyrogram အတွက် Update ကို ကိုင်တွယ်ပါ
        # (ဒီ Bot က Pyrogram သုံးထားတာမို့ Webhook ကို သီးခြားမကိုင်တွယ်ဘူး)
        return "ok", 200
    except Exception as e:
        print(f"Webhook error: {e}")
        return "error", 500

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

def run():
    app.run(
        host="0.0.0.0",
        port=8000
    )

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

def keep_alive():
    Thread(
        target=run
    ).start()

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
