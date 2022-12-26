import os
import logging
import time

from logging.handlers import RotatingFileHandler

APP_ID = 16029596
API_HASH = "8c6b3ce7f23e51dfebbdbe98a0ee674d"
USER_SESSION = "BQCgitgJKfmbC24gezogG8_YLXW_YcC5XlWaFbQcbO4bkNuyl9eNGtNV4wbP4dVPsPDcDuKuCp1wCSx5QozuzOwXzJvWT__ejLYQpCM3T2dLL3N9ElKYAEHzVC0iEbpsHALxI2XrdAGsOd7Rqa5DnvDfr9yzxxEdQQ4omb2ivbM1lu7UIXjntes148DB-_5R1gVcOr8WwZxtT0cOVKG82DpHL2j5J6TiSP8DKhQKltB6QUcSOng8qzRDOkTvA6X5h1DDicP2R0CEleAbIGX1vJSffccRp7wSd84wu3lKCm3usQfOp8MCH5tIjC1dGKRMyGTq-sUNu_YdNotjo-Tr6lNXAAAAAWHA4M8A"
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
