import os
import logging
import time

from logging.handlers import RotatingFileHandler

APP_ID = 26686963
API_HASH = "7cce2717e7e89eb534b7da973926f6c4"
USER_SESSION = "BQAbcBp7IplE9_BJIw05yKC7WZIoUDTFbnXfDLGyIYFpq76tfLLDtlqcfRyZ3rTBgtRxKrZhvsxh1DVzdhxekQuX73dmodoLM8WapEGu390jUb5vHP4y73RwgbHYFYiilMx_FFa60LHH6K1DGzhlk0dvnVn1X634zHvdpW0nmXYhMwH0nUghqSzgXPIJaE_AVHx2ZzMBv-XVluDZZJJIg2Tr2eCg8SNifCz22WJWGbM3VcGm-7VJt6S4wgoAyntndgJx9jvRvpCuOGBJ1h2YdypVh-KDRwpak_4CHubx1NTvYtDzgDzA4grO0UaO1JWURvBvl5I0zUWe2jC2IeSBgj0qAAAAAWHA4M8A"
BOT_TOKEN = "5805452651:AAGIua5po3vFIWsPHm9VZ1umq7oqreenlDw"
MAINCHANNEL_ID = -1001743048821
CAPTION_TEXT = "test message"
FROMCHANNEL_ID = -1001873549778

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "automated.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
