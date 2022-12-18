import os
import logging
import time

from logging.handlers import RotatingFileHandler

APP_ID = 26686963
API_HASH = "7cce2717e7e89eb534b7da973926f6c4"
USER_SESSION = "BQATWCwk7ViMcnfYIk731nkPcraMO2eypd0ME7HMpw-EgZPh_PPld_ef7sM0cGSz5X0W7zxqBg5HhBFf2m5DPauLJiPuhIbl-MZehICJStdBbtW7mC_uymF1AGGfRXvXrIw1GXS5aoIGInX-7Zbp8My-2zJgd9cW1HmRdqC2iuVz5OvwU4MuM8R_k4X3FuMaPCcy9v8wXL2U3i1CNsy_kgjwkr4xom2PNnv06QcxxNNjfD1sL4sUhaLjg_kckZ123360uJywRYc9qGcrfPTrHQdfkFhodZwZtq_mbcTp-Y6xonWTX5pkrIi8z67d96Q9f9ogkOSfTOa0Lxfq6JUxYyShAAAAAVLx0FUA"
BOT_TOKEN = "5300015911:AAE0jwmVovvrv6zH9dC8TfE5-UlFIVOyX78" 
MAINCHANNEL_ID = -1001743048821


VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
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
