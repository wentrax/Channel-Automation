import os, asyncio, logging
from pyrogram.errors import FloodWait
from pyrogram import Client, filters, enums
from bot.importss import Config, Robot
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

media_filter = filters.document | filters.video 

@Client.on_message(filters.chat(-1001860212901) & media_filter)
async def forward(bot, update):
    try:      
        await bot.copy_message(
            chat_id=-1001667023505, 
            from_chat_id=-1001860212901, 
            message_id=update.id, 
            caption=f"**{update.caption}**".replace("DXClassic", "➠ @Hollywood_0980\n➠ @DFF_UPDATES"),             
            parse_mode=enums.ParseMode.MARKDOWN                     
        )
    except FloodWait as e:
        await asyncio.sleep(e.value)


