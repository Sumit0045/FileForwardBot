from pyrogram import filters
from Hancock.core.utils import save_file
from vars import CHANNEL_IDS
from Hancock import app

# -------------------» ᴄʜᴀɴɴᴇʟ «------------------- #

media_filter = filters.document | filters.video | filters.audio


@app.on_message(filters.chat(FORWARD_IDS) & media_filter)
async def media(_, message):
    await app.copy_message(chat_id=CHANNEL_ID, from_chat_id=FORWARD_IDS, message_id=message.id)
