import os
import logging
import time

from logging.handlers import RotatingFileHandler

APP_ID = 16029596
API_HASH = "8c6b3ce7f23e51dfebbdbe98a0ee674d"
USER_SESSION = "BQALHMjzmGN8g3-xOspXRgEyUHnIksKNXGq30TlNrpUlweCSHRqJNIrenNONkwyBvhtbP9V61vQ6zw8C9xc6jWImizDgaIu0zq62sCkr7vHMMcWdAreGgXzqduVPQIwBN2dhlMBMtjSAo3DZUZTtVZwrCbSrBVu0uz2aFZz_oTrjSU98EvusOJxU0_iBes8__Z7wEmh9iTsRJo_-kRYINHiFJgx19hGCnZL7z6cEwByyBkBEP6Wn_TsB-2roTCRQvTcwissthKw2kQDAqOaCQo6G_zWKCClwzOeXk8Dm1bB_HhR41YEIGlArTAfZIjgVeyMLupMafkrzMhYXWAxwUhCGAAAAAUdFtW4A"
BOT_TOKEN = "5975576942:AAEUYPD9wXWxUOO10Ab-0G8aGi_AYYaFY_U"
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
