from bot.info import Config

class Translation(object):

      
      START_TEXT = """
😃 Hai {},
I am a simple auto Channel Automation bot
I am very useful for the channel admin who have many channels.😁

<b>Maintained By:</b> <a href="https://t.me/Lx_0980">Lx 0980</a>
"""    
      COMMANDS_TEXT = """
      <b><u>AVAILABLE COMMAND</b></u>

• /start - <b>Bot Alive</b>

• /help - <b>more help</b>

• /run - <b>start forward</b>

• /about - <b>About Me</b>

• /info - <b>get your telegram ID info.

• /id - <b>Your telegram ID</b
"""


      ABOUT_TEXT = """
MY DETAILS:

</b>🤖 My Name:</b> Channel Automation 

<b>📝 Language:<b> <b><a href="https://www.python.org/">Python</a></b>

<b>🧰 Framework:<b> <b><a href="https://github.com/pyrogram/pyrogram">Pyrogram 2.0.69</a></b>

<b>📢 Channel:<b> <b><a href="https://t.me/Lx0980_Official">Lx0980</a></b>

👥 Group:<b> <b><a href="https://t.me/Hollywood_0980">Hollywood 0980</a></b>
"""
      
      FILES_CAPTION = "`{}`\n\n" + str(Config.FILES_CAPTION)
      COPY_FILES_TEXT = """<b>Follow These Steps!!</b>
<b>• Currectly fill your Heroku Config vars</b> <code>FROM_CHANNEL</code> and <code>TO_CHANNEL</code> <b>and other Vars</b>
<b>• Then give admin permission in your personal telegram channel</b>
<b>• Then send any message In your personal telegram channel</b>
<b>• Then use /run command in your bot</b>
<b><u>Available Command</b></u>

* /run - <b>start forward</b>
"""
