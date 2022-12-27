import os, asyncio, logging
from pyrogram.errors import FloodWait
from pyrogram import Client, filters, enums
from bot.importss import Config 
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

media_filter = filters.document | filters.video 

@Client.on_message(filters.chat(-1001641840781) & media_filter)
async def forward(bot, update):
    try:      
        await bot.copy_message(
            chat_id=-1001840022987, 
            from_chat_id=-1001641840781, 
            message_id=update.id, 
            caption=f"**{update.caption}**".replace("@Latest_Movies_Reborn", " ").replace ("🔥 Fɪʀꜱᴛ Oɴ Tᴇʟᴇɢʀᴀᴍ 🔥", " ").replace("@BollyWeeBHolly", " ").replace("@JESSEVERSE", " ").replace("@Theprofffesorr", " ").replace("\n\n\n", " ") + "\n\n" + "**@DXClassic**",          
            parse_mode=enums.ParseMode.MARKDOWN                     
        )
    except FloodWait as e:
        await asyncio.sleep(e.value)

