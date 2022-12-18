from pyrogram import Client, filters

@Client.on_message(filters.command("start") & filters.private)
async def start(bot, cmd):
      await bot.send_message("Hi there, I'm Auto forward bot")
