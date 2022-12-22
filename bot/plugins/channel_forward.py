import os, asyncio
from pyrogram.errors import FloodWait
from pyrogram import Client, filters, enums

CHANNEL_ID = 1001743048821

@Client.on_message(filters.media)
async def forward(bot, update):
    try:      
        await bot.copy_message(
            chat_id=-1001531149575,
            from_chat_id=-1001688669689,
            message_id=update.id,
            caption=update.caption + "@Lx0980",
            parse_mode=enums.ParseMode.MARKDOWN
        )
        await bot.copy_message(
            chat_id=-1001688669689,
            from_chat_id=-1001743048821,
            message_id=update.id,
            caption=update.caption + "@HQFolms4U",
            parse_mode=enums.ParseMode.MARKDOWN
        )
    except FloodWait as e:
        await asyncio.sleep(e.value)
    
