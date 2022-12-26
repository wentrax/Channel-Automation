import os, asyncio, logging
from pyrogram.errors import FloodWait
from pyrogram import Client, filters, enums
from bot.importss import Config
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

media_filter = filters.document | filters.video 

@Client.on_message(filters.chat(-1001665140291) & media_filter)
async def forward(bot, update):
    try:      
        await bot.copy_message(
            chat_id=-1001531149575, 
            from_chat_id=-1001665140291, 
            message_id=update.id, 
            caption=f"**{update.caption}**".replace("Hollywood_0980", "DXClassic | @Only1DX").replace("@DFF_UPDATES", " ").replace("➠", " "),             
            parse_mode=enums.ParseMode.MARKDOWN                     
        )
    except FloodWait as e:
        await asyncio.sleep(e.value)


