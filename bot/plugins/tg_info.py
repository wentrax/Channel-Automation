from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton(text="UPDATE CHANNEL", url=f"https://t.me/Lx_0980")]])



@Client.on_message(filters.command('id'))
async def showid(client, message):
    chat_type = message.chat.type
    if chat_type == enums.ChatType.PRIVATE:
        user_id = message.chat.id
        first = message.from_user.first_name
        last = message.from_user.last_name or ""
        username = message.from_user.username
        dc_id = message.from_user.dc_id or ""
        await message.reply_text(
            f"**➡️ First Name:** {first}\n<b>➲ Last Name:</b> {last}\n<b>➲ Username:</b> {username}\n<b>➲ Telegram ID:</b> <code>{user_id}</code>\n<b>➲ Data Centre:</b> <code>{dc_id}</code>",
            quote=True
        )

    elif chat_type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        _id = ""
        _id += (
            "**➡️ Chat ID**: "
            f"<code>{message.chat.id}</code>\n"
        )
        if message.reply_to_message:
            _id += (
                "<b>**➡️ User ID</b>**: "
                f"<code>{message.from_user.id if message.from_user else 'Anonymous'}</code>\n"
                "**➡️ Replied User ID**: "
                f"<code>{message.reply_to_message.from_user.id if message.reply_to_message.from_user else 'Anonymous'}</code>\n"
            )
            
        
@Client.on_message(filters.private & filters.command("info"))
async def info(bot, update):    
    text = f"""--<b>Information</b>--
<b>🙋🏻‍♂️ First Name :</b> {update.from_user.first_name}
<b>🧖‍♂️ Your Second Name :</b> {update.from_user.last_name if update.from_user.last_name else 'None'}
<b>🧑🏻‍🎓 Your Username :</b> {update.from_user.username}
<b>🆔 Your Telegram ID :</b> <code>{update.from_user.id}</code>
<b>🔗 Your Profile Link :</b> {update.from_user.mention}"""    
    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
        reply_markup=BUTTONS
    )

@Client.on_message(filters.private & filters.forwarded)
async def forwarded(_, msg):
    if msg.forward_from:
        text = "Forward detected! \n\n"
        if msg.forward_from.is_bot:
            text += "<b>Bot</b>"
        else:
            text += "<b>User</b>"
        text += f'\n{msg.forward_from.first_name} \n'
        if msg.forward_from.username:
            text += f"@{msg.forward_from.username} \nID : <code>{msg.forward_from.id}</code>"
        else:
            text += f'ID : <code>{msg.forward_from.id}</code>'
        await msg.reply(text, quote=True)
    else:
        hidden = msg.forward_sender_name
        if hidden:
            await msg.reply(
                f"Forward detected but unfortunately, {hidden} has enabled forwarding privacy, so I can't get their id",
                quote=True,
            )
        else:
            text = f"Forward Detected. \n\n"
            if msg.forward_from_chat.type == enums.ChatType.CHANNEL:
                text += "<b>Channel</b>"
            if msg.forward_from_chat.type == enums.ChatType.SUPERGROUP:
                text += "<b>Group</b>"
            text += f'\n{msg.forward_from_chat.title} \n'
            if msg.forward_from_chat.username:
                text += f'@{msg.forward_from_chat.username} \n'
                text += f'ID : <code>{msg.forward_from_chat.id}</code>'
            else:
                text += f'ID : <code>{msg.forward_from_chat.id}</code>'
            await msg.reply(text, quote=True)
