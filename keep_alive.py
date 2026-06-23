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
        data = request.get_json(force=True)
        print(f"Webhook received: {data}")
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
