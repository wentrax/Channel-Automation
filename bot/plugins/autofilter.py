import re
import pyrogram

from pyrogram import filters, Client, enums


from pyrogram.types import (
    InlineKeyboardButton, 
    InlineKeyboardMarkup, 
    Message,
    CallbackQuery
)

from bot.importss import Robot as Bot
from bot.info import Config

document = enums.MessagesFilter.DOCUMENT
BUTTONS = {}
 
@Client.on_message(filters.group & filters.text)
async def filter(client: Bot, message: Message):
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
        return

    if len(message.text) > 2:    
        btn = []
        async for msg in client.USER.search_messages(Config.FILTERCHANNEL_ID,query=message.text,filter=document):
            file_name = msg.document.file_name
            msg_id = msg.id                     
            link = msg.link
            btn.append(
                [InlineKeyboardButton(text=f"{file_name}",url=f"{link}")]
            )

        if not btn:
            return

        if len(btn) > 5: 
            btns = list(split_list(btn, 5)) 
            keyword = f"{message.chat.id}-{message.id}"
            BUTTONS[keyword] = {
                "total" : len(btns),
                "buttons" : btns
            }
        else:
            buttons = btn
            buttons.append(
                [InlineKeyboardButton(text="📃 Pages 1/1",callback_data="pages")]
            )
            await message.reply_text(
                f"<b> Here is the result for {message.text}</b>",
                reply_markup=InlineKeyboardMarkup(buttons)
            )
            return

        data = BUTTONS[keyword]
        buttons = data['buttons'][0].copy()

        buttons.append(
            [InlineKeyboardButton(text="NEXT ⏩",callback_data=f"next_0_{keyword}")]
        )    
        buttons.append(
            [InlineKeyboardButton(text=f"📃 Pages 1/{data['total']}",callback_data="pages")]
        )

        await message.reply_text(
                f"<b> Here is the result for {message.text}</b>",
                reply_markup=InlineKeyboardMarkup(buttons)
            )    


@Client.on_callback_query()
async def cb_handler(client: Bot, message: Message, update: CallbackQuery):
    if update.message.reply_to_message.from_user.id == update.from_user.id:

        if update.data.startswith("next"):
            await update.answer()
            ident, index, keyword = update.data.split("_")
            data = BUTTONS[keyword]

            if int(index) == int(data["total"]) - 2:
                buttons = data['buttons'][int(index)+1].copy()

                buttons.append(
                    [InlineKeyboardButton("⏪ BACK", callback_data=f"back_{int(index)+1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📃 Pages {int(index)+2}/{data['total']}", callback_data="pages")]
                )

                await update.edit_message_reply_markup( 
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

                await update.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return


        elif update.data.startswith("back"):
            await update.answer()
            ident, index, keyword = update.data.split("_")
            data = BUTTONS[keyword] 

            if int(index) == 1:
                buttons = data['buttons'][int(index)-1].copy()

                buttons.append(
                    [InlineKeyboardButton("NEXT ⏩", callback_data=f"next_{int(index)-1}_{keyword}")]
                )
                buttons.append(
                    [InlineKeyboardButton(f"📃 Pages {int(index)}/{data['total']}", callback_data="pages")]
                )

                await update.edit_message_reply_markup( 
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

                await update.edit_message_reply_markup( 
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                return


        elif update.data == "pages":
            await update.answer()

    else:
        await update.answer("Thats not for you!!",show_alert=True)



def split_list(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]
