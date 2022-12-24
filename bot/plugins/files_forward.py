import asyncio, sys, os, logging
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import FloodWait
from bot.importss import Config, Translation
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

FROM = Config.FILES_FROM_CHANNEL
TO = Config.FILES_TO_CHANNEL

rpl1c = "➠ @Hollywood_0980 ✅\n➠ @DFF_UPDATE"

rpl2c = "@Hollywood_0980"
rpl3c = "@LkLMNL_09870"
rpl4c = "➠ @Hollywood_0980\n➠ @DFF_UPDATE"
rpl5c = " ➠ @Hollywood_0980\n➠ @DFF_UPDATES"

rplcd = "@DXClassic | @Only1DX"
"""
CODE = replace(
         rpl1c, 
         rplcd
       ).replace(
         rpl2c, 
         rplcd).replace(rpl3c, rplcd).replace(rpl4c, rplcd).replace(rpl5c, rplcd)
"""
document = enums.MessagesFilter.DOCUMENT 

@Client.on_message(filters.private & filters.command(["start_forward"]))
async def run(bot, message):
    if str(message.from_user.id) not in Config.ADMIN_ID:
        return
    buttons = [[
        InlineKeyboardButton('🚫 STOP', callback_data='stop_btn')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    m = await bot.send_message(
        text="<i>File Forwording Started😉</i>",
        reply_markup=reply_markup,
        chat_id=message.chat.id
    )

    files_count = 0
    async for message in bot.USER.search_messages(chat_id=FROM,filter=document):
        try:
            if message.video:
                file_name = message.video.file_name
            elif message.document:
                file_name = message.document.file_name
            elif message.audio:
                file_name = message.audio.file_name
            else:
                file_name = None               
            await bot.copy_message(
                chat_id=TO,
                from_chat_id=FROM,
                parse_mode=enums.ParseMode.MARKDOWN,       
                caption=message.replace(rpl1c, rplcd).replace(rpl2c, rplcd).replace(rpl3c, rplcd).replace(rpl4c, rplcd).replace(rpl5c, rplcd),
                message_id=message.id
            )
            files_count += 1
            await asyncio.sleep(1)
        except FloodWait as e:
            await asyncio.sleep(e.value) 
        except Exception as e:
            print(e)
            pass
   # await m.delete()
    buttons = [[
        InlineKeyboardButton('📜 Channel', url='https://t.me/Lx0980_Official')
    ]] 
    reply_markup = InlineKeyboardMarkup(buttons)
    await m.edit(
        text=f"<u><i>Successfully Forwarded</i></u>\n\n<b>Total Forwarded Files:-</b> <code>{files_count}</code> <b>Files</b>\n<b>Thanks For Using Me❤️</b>",
        reply_markup=reply_markup
    )
        

@Client.on_callback_query(filters.regex(r'^stop_btn$'))
async def stop_button(c: Client, cb: CallbackQuery):
    await cb.message.delete()
    await cb.answer()
    msg = await c.send_message(
        text="<i>Trying To Stoping.....</i>",
        chat_id=cb.message.chat.id
    )
    await asyncio.sleep(5)
    await msg.edit("<i>File Forword Stoped Successfully 👍</i>")
    os.execl(sys.executable, sys.executable, *sys.argv)
    
@Client.on_callback_query(filters.regex(r'^close_btn$'))
async def close(bot, update):
    await update.answer()
    await update.message.delete()
