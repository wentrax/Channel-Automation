from pyrogram import Client, enums, __version__
from AutoForward import API_HASH, APP_ID, LOGGER, \
    USER_SESSION
from AutoForward.bot import Lxbot

class User(Client):
    LXBOT: Lxbot = None
    LXBOT_ID = 5300015911

    def __init__(self):
        super().__init__(            
            name='user_session',
            session_string=USER_SESSION,
            api_hash=API_HASH,
            api_id=APP_ID,
            workers=200,            
            sleep_threshold=10,
            plugins={
                "root": "AutoForward/plugins"
            }
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        user_details = await self.get_me()
        self.set_parse_mode(enums.ParseMode.HTML)
        self.LOGGER(__name__).info(
            f"@{user_details.username}  started! "
        )
        self.LXBOT, LXBOT_ID = await Lxbot().start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
