import os, asyncio, logging
from pyrogram.errors import FloodWait
from pyrogram import Client, filters, enums
from bot.importss import Config 
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

media_filter = filters.document | filters.video 

@Client.on_message(filters.chat(-1001720280064) & media_filter)
async def forward(bot, update):
    try:      
        await bot.copy_message(
            chat_id=-1001929344696, 
            from_chat_id=-1001720280064, 
            message_id=update.id, 
            caption=update.caption, 
            parse_mode=enums.ParseMode.MARKDOWN                     
        )
    except FloodWait as e:
        await asyncio.sleep(e.value)

