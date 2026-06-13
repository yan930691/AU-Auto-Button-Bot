from config import LOG_CHANNEL


async def send_log(client, text):

    if not LOG_CHANNEL:
        return

    try:

        await client.send_message(
            chat_id=LOG_CHANNEL,
            text=f"""
📌 <b>BOT LOG</b>

{text}
""",
            parse_mode="HTML"
        )

    except Exception as e:

        print(
            f"LOG ERROR: {e}"
        )
