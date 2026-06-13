# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

from config import LOG_CHANNEL

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #

async def send_log(
    client,
    text
):

    try:

        await client.send_message(
            LOG_CHANNEL,
            text
        )

    except:

        pass

# ------------------------- #
# Don't Remove Credit 
# Owner @Mr_Mohammed_29
# ------------------------- #
