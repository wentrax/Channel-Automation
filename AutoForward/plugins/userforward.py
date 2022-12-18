import logging, asyncio
logger = logging.getLogger(__name__)
from AutoForward import MAINCHANNEL_ID
from pyrogram import Client, filters, enums
from AutoForward.client import User
from pyrogram.errors import FloodWait

CHANNEL_ID = 1001743048821

@Client.on_message(filters.media)
async def forward(client, update):
    try:      
        await asyncio.sleep(15)
        await client.copy_message(
            chat_id=-1001743048821,
            from_chat_id=-1001531149575,
            message_id=update.id.replace("Latest_Movies_Reborn", "DXClassiC"),
            caption=update.caption,
            parse_mode=enums.ParseMode.MARKDOWN
        )
    except FloodWait as e:
        await asyncio.sleep(e.value)
