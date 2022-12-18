from pyrogram import Client, filters

@autocaption.on_message(filters.command("start") & filters.incoming)
async def start(bot, message):
        await message.reply(" Hello, I'm Auto Forward Bot")
