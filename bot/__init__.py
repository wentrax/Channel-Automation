import os
import logging
import time

from logging.handlers import RotatingFileHandler

APP_ID = 26686963
API_HASH = "7cce2717e7e89eb534b7da973926f6c4"
USER_SESSION = "BQBSW_rj0ZGhtmyZitn2yRX68UjivVPgw7Q7cw59zvGgTyrn_yK0oknLinI7M9XpkvQSYo3UY4-TQ2oLD20w4UUMB5CIpK8HVbkitPf9-G_xybkKafUXz5Q2Ub7h4153cuKYJRkrA0k3dKFh3tPjgR4PcIyl5OabBQXGvyXTXpn_wZUEmm1fIPR398yEw7NuQtRWn7SSdGXkDNbEsUmITpDDreT4tX6Ho3o9GpYGxuzxG0eb5fn_3eori7t7Z2ZpgJ1pJOL7o1CPVmhky7EJgYYdLNnvXaIA5EAjrRo8S-8oFMWbm35akKIoAUknGq19iWVJN1N_hqYeN_6P6EUH2IZgAAAAAWHA4M8A"
BOT_TOKEN = "5975576942:AAEKAlb4FgK0CvXRxuR0x69gog2nKISTFH8"
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
