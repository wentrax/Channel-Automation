from pyrogram import filters, enums
from bot.importss import Config, Translation, Robot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Robot.on_callback_query()
async def button(bot, update: CallbackQuery):
    cb_data = update.data
    if "about_data" in cb_data:
        await update.message.edit(
             text = Translation.ABOUT_TEXT,
             parse_mode = enums.ParseMode.MARKDOWN, 
             disable_web_page_preview=True, 
             reply_markup=InlineKeyboardMarkup(
                 [
                     [
                      InlineKeyboardButton("⬇️ BACK", callback_data="home_data"),
                      InlineKeyboardButton("🔐 CLOSE", callback_data="close_data")
                     ]
 
                 ] 
             ) 
        )
    elif "commands_data" in cb_data:
          await update.message.edit(
               text=Translation.COMMANDS_TEXT,
               parse_mode = enums.ParseMode.HTML, 
               disable_web_page_preview=True, 
               reply_markup=InlineKeyboardMarkup(
                   [
                       [
                        InlineKeyboardButton("⬇️ BACK", callback_data="home_data"),
                        InlineKeyboardButton("🔐 CLOSE", callback_data="close_data")
                       ]
 
                   ] 
               ) 
          )
    elif "home_data" in cb_data:
          await update.message.edit(
               text=Translation.START_TEXT.format(update.from_user.first_name, Config.ADMIN_USERNAME),
               parse_mode = enums.ParseMode.MARKDOWN, 
               disable_web_page_preview=True, 
               reply_markup=InlineKeyboardMarkup(
                   [
                      
                       [
                        InlineKeyboardButton("📫 UPDATES", url="https://t.me/Lx0980_Official"),
                        InlineKeyboardButton("📕 ABOUT ME", callback_data="about_data")
                       ],[                       
                        InlineKeyboardButton("💡 HELP", callback_data="commands_data")
                       ]
                   ]
               )
          )
    elif "close_data" in cb_data:
          await update.message.delete()
          await update.message.reply_to_message.delete()


