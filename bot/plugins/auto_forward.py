import os, asyncio
from pyrogram.errors import FloodWait
from pyrogram import Client, filters, enums
from bot.importss import Config 

media_filter = filters.document | filters.video 

@Client.on_message(filters.chat(-1001641840781) & media_filter)
async def forward(bot, update):
    try:      
        await bot.copy_message(
            chat_id=-1001427335527, 
            from_chat_id=-1001641840781, 
            message_id=update.id, 
            caption=f"**{update.caption}**".replace("Latest_Movies_Reborn", "DXClassic"),             
            parse_mode=enums.ParseMode.MARKDOWN                     
        )
    except FloodWait as e:
        await asyncio.sleep(e.value)

@Client.on_message(filters.chat(-1001665140291) & media_filter)
async def forward(bot, update):
    try:      
        await bot.copy_message(
            chat_id=-1001531149575, 
            from_chat_id=-1001665140291, 
            message_id=update.id, 
            caption=f"**{update.caption}**".replace("Hollywood_0980", "DXClassic"),             
            parse_mode=enums.ParseMode.MARKDOWN                     
        )
    except FloodWait as e:
        await asyncio.sleep(e.value)
