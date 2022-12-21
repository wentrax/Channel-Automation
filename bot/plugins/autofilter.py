import re
import pyrogram

from pyrogram import filters, Client, enums


from pyrogram.types import (
    InlineKeyboardButton, 
    InlineKeyboardMarkup, 
    Message,
    CallbackQuery
)

from bot.importss import Robot
from bot.info import Config

document = enums.MessagesFilter.DOCUMENT
BUTTONS = {}
 
@Client.on_message(filters.group & filters.text)
async def filter(client: Robot, message: Message):
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

        if len(btn) > 10: 
            btns = list(split_list(btn, 10)) 
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

def split_list(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]  
