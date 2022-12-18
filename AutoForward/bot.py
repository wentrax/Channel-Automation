from pyrogram import Client, enums, __version__

from AutoForward import API_HASH, APP_ID, LOGGER, BOT_TOKEN 

class Lxbot(Client):
    def __init__(self):
        super().__init__(
            name='bot',
            bot_token=BOT_TOKEN,
            api_hash=API_HASH,
            api_id=APP_ID,
            workers=8
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        myusername = await self.get_me()
        self.set_parse_mode(enums.ParseMode.HTML)
        self.LOGGER(__name__).info(
            f"@{myusername.username}  started!"
        )
        

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
