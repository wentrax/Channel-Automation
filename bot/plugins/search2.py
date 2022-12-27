import re, pyrogram, logging
from pyrogram import filters, enums, Client
from bot.importss import Config, Translation, Robot
from bot.importss import Robot as Bot
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
# from .search import BUTTON 

BUTTON = {}

MEDIA_FILTER = enums.MessagesFilter.VIDEO 

@Client.on_message(filters.chat([-1001589825618, -1001779657158]) & filters.text)
async def search(client: Bot, message: Message):
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", message.text):
        return
    if len(message.text) > 2:    
        btn = []
        async for msg in client.USER.search_messages(Config.AUTO_2_FILTER,query=message.text,filter=MEDIA_FILTER):
            file_name = msg.video.file_name
            msg_id = msg.id                     
            link = msg.link
            btn.append(
                [InlineKeyboardButton(text=f"{file_name}",url=f"{link}")]
            )

        if not btn:
            return

        if len(btn) > 5: 
            btns = list(split_lists(btn, 5)) 
            keyword = f"{message.chat.id}-{message.id}"
            BUTTON[keyword] = {
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

        data = BUTTON[keyword]
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

def split_lists(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]  



