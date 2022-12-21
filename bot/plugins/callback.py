
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




@Client.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    if query.message.reply_to_message.from_user.id == query.from_user.id:

        if query.data.startswith("next"):
            await query.answer()
            ident, index, keyword = query.data.split("_")
            data = BUTTONS[keyword]

            if int(index) == int(data["total"]) - 2:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("⏪ BACK", callback_data=f"back_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📃 Pages {int(index)+2}/{data['total']}", callback_data="pages")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return
            else:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("⏪ BACK", callback_data=f"back_{int(index)+1}_{keyword}"),InlineKeyboardButton("NEXT ⏩", callback_data=f"next_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📃 Pages {int(index)+2}/{data['total']}", callback_data="pages")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return


        elif query.data.startswith("back"):
            await query.answer()
            ident, index, keyword = query.data.split("_")
            data = BUTTONS[keyword] 

            if int(index) == 1:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("NEXT ⏩", callback_data=f"next_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📃 Pages {int(index)}/{data['total']}", callback_data="pages")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return   
            else:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("⏪ BACK", callback_data=f"back_{int(index)-1}_{keyword}"),InlineKeyboardButton("NEXT ⏩", callback_data=f"next_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📃 Pages {int(index)}/{data['total']}", callback_data="pages")]
                )

                await query.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return


        elif query.data == "pages":
            await query.answer()

       
    else:
        await query.answer("Thats not for you!!",show_alert=True)

