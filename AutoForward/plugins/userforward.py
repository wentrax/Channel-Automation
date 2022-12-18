# @Lx0988
import logging, asyncio
logger = logging.getLogger(__name__)
from AutoForward import FROMCHANNEL_ID
from pyrogram import Client, filters, enums
from pyrogram.errors import FloodWait

 
@Client.on_message(filters.media)
async def forward(client, update):
    try:      
        await asyncio.sleep(10)
        await client.copy_message(
            chat_id=-1001688669689,
            from_chat_id=FROMCHANNEL_ID,
            message_id=update.id,
            caption=update.caption,
            parse_mode=enums.ParseMode.MARKDOWN
        )

    except FloodWait as e:
        await asyncio.sleep(e.value)
