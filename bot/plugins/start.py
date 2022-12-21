import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.importss import Translation, Robot, Config 
from bot.database import *

#all buttons 

#start buttons 

start_button=InlineKeyboardMarkup(
        [
              [
                  InlineKeyboardButton("📄 BOT STATUS", callback_data = "status_data")
              ], 
              [
                  InlineKeyboardButton("📫 UPDATES", url = "https://t.me/Ts_bots"), 
                  InlineKeyboardButton("📕 ABOUT", callback_data = "about_data")
              ], 
              [
                  InlineKeyboardButton("💡 HELP", callback_data = "help_data"), 
                  InlineKeyboardButton("🔐 CLOSE", callback_data = "close_data")
              ] 
        ]
)

# help buttons

help_button=InlineKeyboardMarkup(
        [
              [
                InlineKeyboardButton("ABOUT MARKDOWN", callback_data = "markdown_data")
              ], 
              [
                  InlineKeyboardButton("⬇️ BACK", callback_data = "back_data"), 
                  InlineKeyboardButton("🔐 CLOSE", callback_data = "close_data")
              ]
        ]
)
 
# about button 

about_button=InlineKeyboardMarkup(
        [
              [
                  InlineKeyboardButton("⬇️ BACK", callback_data = "back_data"), 
                  InlineKeyboardButton("🔐 CLOSE", callback_data = "close_data")
              ]
        ]
) 


@Robot.on_message(filters.command("start") & filters.private)
async def start(bot, update):
      await bot.send_message(
          chat_id = update.chat.id,
          text = Translation.START_TEXT.format(update.from_user.first_name, Config.ADMIN_USERNAME), 
          reply_to_message_id = update.id,
          parse_mode = enums.ParseMode.MARKDOWN,
          disable_web_page_preview = True, 
          reply_markup = start_button
      )


@Robot.on_message(filters.command("help") & filters.private)
async def help(bot, update):
      await bot.send_message(
          chat_id = update.chat.id,
          text = Translation.HELP_TEXT, 
          reply_to_message_id = update.id,
          parse_mode = enums.ParseMode.HTML,
          disable_web_page_preview = True,
          reply_markup = help_button           
      )


@Robot.on_message(filters.command("about") & filters.private)
async def about(bot, update):
      await bot.send_message(
          chat_id = update.chat.id,
          text = Translation.ABOUT_TEXT, 
          reply_to_message_id = update.id,
          parse_mode = enums.ParseMode.MARKDOWN,
          disable_web_page_preview = True, 
          reply_markup = about_button
      )   


@Robot.on_message(filters.command("set_caption") & filters.private)
async def set_caption(bot, update):
    if Config.ADMIN_ID != update.from_user.id:
        return

    if len(update.command) == 1:
        await update.reply_text(
            "🖊️ 𝐒𝐄𝐓 𝐂𝐀𝐏𝐓𝐈𝐎𝐍 \n\nUse this command to set your own caption text \n\n👉 `set_caption My Caption`", 
            quote = True
        )
    else:
        command, caption = update.text.split(' ', 1)
        await update_caption(update.from_user.id, caption)
        await update.reply_text(f"**--Your Caption--:**\n\n{caption}", quote=True)




