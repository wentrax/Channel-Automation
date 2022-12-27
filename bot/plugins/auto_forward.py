import os, asyncio, logging
from pyrogram.errors import FloodWait
from pyrogram import Client, filters, enums
from bot.importss import Config 
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

media_filter = filters.document | filters.video 

@Client.on_message(filters.chat(-1001857977699) & media_filter)
async def forward(bot, update):
    try:      
        await bot.copy_message(
            chat_id=-1001846691219, 
            from_chat_id=-1001857977699, 
            message_id=update.id, 
            caption=f"**{update.caption}**".replace("@Latest_Movies_Reborn", " ").replace ("🔥 Fɪʀꜱᴛ Oɴ Tᴇʟᴇɢʀᴀᴍ 🔥", " ").replace("@BollyWeeBHolly", " ").replace("@JESSEVERSE", " ").replace("@Theprofffesorr", " "),          
            parse_mode=enums.ParseMode.MARKDOWN                     
        )
    except FloodWait as e:
        await asyncio.sleep(e.value)

@Client.on_message(filters.chat(-1001427335527) & media_filter)
async def forward_2_auto(bot, update):
    try:      
        await bot.copy_message(
            chat_id=-1001667023505, 
            from_chat_id=-1001427335527, 
            message_id=update.id, 
            caption=f"**{update.caption}**".replace("@DXClassic", "➠ @Hollywood_0980\n➠ @DFF_UPDATES"),
            parse_mode=enums.ParseMode.MARKDOWN                     
        )
    except FloodWait as e:
        await asyncio.sleep(e.value)
