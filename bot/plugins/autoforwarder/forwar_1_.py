import os, asyncio
from pyrogram.errors import FloodWait
from pyrogram import Client, filters, enums

@Client.on_message(filters.media)
async def forward(bot, update):
    try:      
        await bot.copy_message(
            chat_id=-1001840022987,
            from_chat_id=-1001793975460,
            message_id=update.id,
            caption=update.caption, # }**".replace("Latest_Movies_Reborn", "**HQFilms4U**"), # + "\n\n" "<b>@HQFilms4U</b>",       
            parse_mode=enums.ParseMode.MARKDOWN
        )              
    except FloodWait as e:
        await asyncio.sleep(e.value)
