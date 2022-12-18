import os
import logging
import time

from logging.handlers import RotatingFileHandler

APP_ID = 26686963
API_HASH = "7cce2717e7e89eb534b7da973926f6c4"
USER_SESSION = "BQATWCwk7ViMcnfYIk731nkPcraMO2eypd0ME7HMpw-EgZPh_PPld_ef7sM0cGSz5X0W7zxqBg5HhBFf2m5DPauLJiPuhIbl-MZehICJStdBbtW7mC_uymF1AGGfRXvXrIw1GXS5aoIGInX-7Zbp8My-2zJgd9cW1HmRdqC2iuVz5OvwU4MuM8R_k4X3FuMaPCcy9v8wXL2U3i1CNsy_kgjwkr4xom2PNnv06QcxxNNjfD1sL4sUhaLjg_kckZ123360uJywRYc9qGcrfPTrHQdfkFhodZwZtq_mbcTp-Y6xonWTX5pkrIi8z67d96Q9f9ogkOSfTOa0Lxfq6JUxYyShAAAAAVLx0FUA"
BOT_TOKEN = "5300015911:AAGRaVvGt6aKFihpSX3yf2DZ0M2PpYGMGnk" 
MAINCHANNEL_ID = -1001743048821
USER_2_SESSION = "BQCuf6fIhjYjX8dXuooezpbVcbsEJ1X_cDooXgFb8AiqcZRr36bwsLwqNesVA8Qr2B-4QSVEl2WbwEHIJuA-RzQF9S4bHETzpl374lq48SjWC1rLekXkGq5y5oVT4DTk3dRcYq1lLkBTnzdJqXOK1vyn_ndq8EB2Dp3lqJlD_Tw4dWzNbeHKDyLc8DRi8Fn2d1NK2dJ4YfBv-JeGDvIARGKMdlvsS-lgHLqflscKrHp6fi_RXapLltW0EsDifIFeEsF27L6rtHsW_wU72mmg17NVcwsg9cvFRtWs790tUtcOcD-PljS-kEo8Sc2YGjGWHqHTUUNbWjsrsTUkZIv9iOwVAAAAAUSZaVUA"

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
