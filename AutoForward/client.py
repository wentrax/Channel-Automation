from pyrogram import Client, enums, __version__
from AutoForward import API_HASH, APP_ID, LOGGER, \
    USER_SESSION
from AutoForward.UserClients import User2nd

class User(Client):
    USER2ND: User2nd = None
    USER2ND_ID: int = None

    def __init__(self):
        super().__init__(
            "userbot",
            api_hash=API_HASH,
            api_id=APP_ID,
            session_string=USER_SESSION,
            workers=20,
            plugins={
                "root": "AutoForward/plugins"
            }
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        try: await self.export_session_string()
        except: pass
        usr_bot_me = await self.get_me()
        return (self, usr_bot_me.id)
        self.USER2ND, self.USER2ND_ID = await User2nd().start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
