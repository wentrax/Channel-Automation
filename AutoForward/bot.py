from pyrogram import Client, enums, __version__

from AutoForward import API_HASH, APP_ID, LOGGER, USER_2_SESSION

class User2(Client):
    def __init__(self):
        super().__init__(
            "userbot",
            api_hash=API_HASH,
            api_id=APP_ID,
            session_string=USER_2_SESSION,
            workers=20
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        try: await self.export_session_string()
        except: pass
        usr_bot_me = await self.get_me()
        return (self, usr_bot_me.id)

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
