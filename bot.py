# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

import os
import logging
import re
from flask import Flask, request
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# ---------- Config ----------
# 🔥 BOT_TOKEN ရော TELEGRAM_TOKEN ရော နှစ်ခုလုံး အလုပ်လုပ်မယ်
TOKEN = os.environ.get("TELEGRAM_TOKEN") or os.environ.get("BOT_TOKEN")
if not TOKEN:
    logger.error("TELEGRAM_TOKEN not set")
    exit(1)

ADMIN_ID = int(os.environ.get("ADMIN_ID", 0))

def is_admin(user_id):
    return user_id == ADMIN_ID

# ---------- Helper Functions ----------
def extract_deeplink_and_name(text):
    url_match = re.search(r'https://t\.me/[^\s]+', text)
    if not url_match:
        return None, None
    url = url_match.group(0)
    name = text.replace(url, '').strip()
    if not name:
        name = "Episode"
    return url, name

def extract_season_episode_from_name(name):
    if not name:
        return None, None
    patterns = [
        r'(?:S|Season)\s*(\d+)\s*(?:E|Episode)\s*(\d+)',
        r's(\d+)e(\d+)',
        r'(\d+)x(\d+)',
    ]
    for pattern in patterns:
        match = re.search(pattern, name, re.IGNORECASE)
        if match:
            return int(match.group(1)), int(match.group(2))
    return None, None

def extract_movie_title_from_name(name):
    if not name:
        return "Movie"
    cleaned = re.sub(r'(?:S|Season)\s*\d+\s*(?:E|Episode)\s*\d+', '', name, flags=re.IGNORECASE)
    cleaned = re.sub(r's\d+e\d+', '', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\d+x\d+', '', cleaned)
    cleaned = re.sub(r'\(\d{4}\)', '', cleaned)
    cleaned = re.sub(r'\b\d{3,4}p\b', '', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\b(MPK|MKV|MP4|AVI|x264|x265|HEVC)\b', '', cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r'\s+', ' ', cleaned)
    cleaned = cleaned.strip()
    return cleaned or "Movie"

# ---------- Commands ----------
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id != ADMIN_ID:
        await update.message.reply_text("⛔ ခွင့်မပြုပါ။")
        return
    await update.message.reply_text(
        "🎥 **Button Creator Bot**\n\n"
        "📌 **ညွှန်ကြားချက်:**\n"
        "1️⃣ `/post` နှိပ်ပြီး Post အသစ်စတင်ပါ။\n"
        "2️⃣ Poster (ပုံ) → Caption (စာသား) ပို့ပါ။\n"
        "3️⃣ Deep Link တွေ ဆက်တိုက်ပို့ပါ။\n"
        "4️⃣ အကုန်ပို့ပြီးရင် `/done` နှိပ်ပါ။"
    )

async def post_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id != ADMIN_ID:
        await update.message.reply_text("⛔ ခွင့်မပြုပါ။")
        return
    context.user_data.clear()
    context.user_data['step'] = 'waiting_poster'
    await update.message.reply_text("🖼️ Poster (ပုံ) ကို ပို့ပါ။")

async def done_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id != ADMIN_ID:
        await update.message.reply_text("⛔ ခွင့်မပြုပါ။")
        return
    
    poster = context.user_data.get('temp_poster')
    caption_text = context.user_data.get('temp_caption')
    links = context.user_data.get('temp_links', [])
    
    if not poster:
        await update.message.reply_text("⚠️ Poster (ပုံ) အရင်ပို့ပါ။")
        return
    if not caption_text:
        await update.message.reply_text("⚠️ Caption (စာသား) အရင်ပို့ပါ။")
        return
    if not links:
        await update.message.reply_text("⚠️ အနည်းဆုံး Deep Link တစ်ခုတော့ ပို့ပေးပါ။")
        return
    
    seasons = {}
    for link_data in links:
        url = link_data['url']
        name = link_data['name']
        s, e = extract_season_episode_from_name(name)
        movie_name = extract_movie_title_from_name(name)
        if s and e:
            button_text = f"{movie_name} Season {s} Episode {e} ရယူရန်"
            season_key = str(s)
        else:
            button_text = name[:30]
            season_key = "0"
        if season_key not in seasons:
            seasons[season_key] = []
        seasons[season_key].append({'text': button_text, 'url': url, 'episode': e or 0})
    
    total_episodes = sum(len(links) for links in seasons.values())
    await update.message.reply_text(f"⏳ Post ဆောက်နေပါတယ်... (Seasons: {len(seasons)}, Episodes: {total_episodes})")
    
    try:
        keyboard = []
        for season_num in sorted(seasons.keys(), key=int):
            season_links = sorted(seasons[season_num], key=lambda x: x.get('episode', 0))
            if season_num == "0":
                header_text = "─── အခြား အပိုင်းများ ───"
            else:
                header_text = f"─── အတွဲ {season_num} (အပိုင်းပေါင်း: {len(season_links)}) ───"
            keyboard.append([InlineKeyboardButton(header_text, callback_data="none")])
            for link_data in season_links:
                keyboard.append([InlineKeyboardButton(link_data['text'], url=link_data['url'])])
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        final_caption = f"🎬 **{caption_text}**\n\n📥 အောက်ပါခလုတ်များကို နှိပ်ပြီး ကြည့်ရှု့ပါ။"
        await update.message.reply_photo(photo=poster, caption=final_caption, reply_markup=reply_markup, parse_mode='Markdown')
        await update.message.reply_text(f"✅ **Post ကို သင့်ဆီကိုပဲ ပို့လိုက်ပါပြီ။**\n\n📊 Season {len(seasons)} ခု၊ Episode {total_episodes} ခု ပါဝင်ပါတယ်။\n\n💡 Channel မှာ ပြန်တင်ချင်ရင် ဒီ Post ကို Forward လုပ်ပါ။")
    except Exception as e:
        await update.message.reply_text(f"❌ Post တင်ရာမှာ အမှားရှိသွားတယ်။ ကျေးဇူးပြုပြီး နောက်မှ ပြန်ကြိုးစားပါ။")
        logger.error(f"Post error: {e}")
    context.user_data.clear()

async def cancel_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id != ADMIN_ID:
        await update.message.reply_text("⛔ ခွင့်မပြုပါ။")
        return
    context.user_data.clear()
    await update.message.reply_text("✅ လုပ်ဆောင်နေတာကို ဖျက်လိုက်ပါပြီ။")

# ---------- Handlers ----------
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id != ADMIN_ID:
        return
    step = context.user_data.get('step')
    if step != 'waiting_poster':
        await update.message.reply_text("⚠️ ကျေးဇူးပြုပြီး `/post` နဲ့ အရင်စတင်ပါ။")
        return
    photo = update.message.photo[-1]
    context.user_data['temp_poster'] = photo.file_id
    context.user_data['step'] = 'waiting_caption'
    await update.message.reply_text("✅ ပိုစတာ သိမ်းဆည်းပြီးပါပြီ။ Caption (စာသား) ကို ပို့ပါ။")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id != ADMIN_ID:
        return
    text = update.message.text.strip()
    if text.startswith('/'):
        return
    step = context.user_data.get('step')
    
    if step == 'waiting_caption':
        context.user_data['temp_caption'] = text
        context.user_data['step'] = 'waiting_links'
        await update.message.reply_text("✅ Caption သိမ်းဆည်းပြီးပါပြီ။\n\n🔗 Deep Link တွေ စတင်ပို့ပါ။\n✅ အကုန်ပို့ပြီးရင် `/done` နှိပ်ပါ။")
        return
    
    if step == 'waiting_links':
        url, name = extract_deeplink_and_name(text)
        if not url:
            await update.message.reply_text("⚠️ Deep Link မတွေ့ပါ။ `https://t.me/...` ပါတဲ့ Message ကို ပို့ပါ။")
            return
        if 'temp_links' not in context.user_data:
            context.user_data['temp_links'] = []
        context.user_data['temp_links'].append({'url': url, 'name': name})
        total = len(context.user_data['temp_links'])
        await update.message.reply_text(f"✅ Link #{total} သိမ်းဆည်းပြီးပါပြီ။\n✅ ဆက်ပို့နိုင်ပါတယ်။\n✅ အကုန်ပြီးရင် `/done` နှိပ်ပါ။")
        return
    
    await update.message.reply_text("⚠️ နားမလည်ပါ။\n\n📌 `/post` - Post အသစ်စတင်ရန်\n📌 `/done` - Post တင်ရန်\n📌 `/cancel` - ဖျက်ရန်")

# ---------- Flask Webhook ----------
telegram_app = ApplicationBuilder().token(TOKEN).build()
telegram_app.add_handler(CommandHandler("start", start_command))
telegram_app.add_handler(CommandHandler("post", post_command))
telegram_app.add_handler(CommandHandler("done", done_command))
telegram_app.add_handler(CommandHandler("cancel", cancel_command))
telegram_app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
telegram_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json(force=True)
        update = Update.de_json(data, telegram_app.bot)
        telegram_app.process_update(update)
        return "ok", 200
    except Exception as e:
        logger.error(f"Webhook error: {e}")
        return "error", 500

@app.route('/', methods=['GET'])
def health():
    return "Bot is running!", 200

# ---------- Main ----------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
