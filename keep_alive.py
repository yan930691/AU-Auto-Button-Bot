from flask import Flask, request
from threading import Thread
import json
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json(force=True)
        # ဒီနေရာမှာ Update ကို ကိုင်တွယ်ပါ
        print(f"Webhook received: {data}")
        return "ok", 200
    except Exception as e:
        print(f"Webhook error: {e}")
        return "error", 500

def run():
    app.run(host="0.0.0.0", port=8000)

def keep_alive():
    Thread(target=run).start()
