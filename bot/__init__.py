import os
import logging
import time

from logging.handlers import RotatingFileHandler

APP_ID = 16448144
API_HASH = "1073665850700150caf0e0cbb68216a2"
USER_SESSION = "AgAleW_Yhgs8k9Z13LLGk9DpJa3S7CrgcsjZCaNBGEW1_CEunlLmkO_K9fj0AzREV6xv5VAdw6vznxBf0zbeUxdSFFdFsoGoR6kfXRSXJLl71dVUGU0QOG56BnCR65Ljr4qFM_QUJ7ppYvBSuYTQbpu42xaHobz497GpCFUn_cykxiJTRmTT-P1tfDusxNCIaUAG4ehfnHAhc85kP4p9OjljmWouRgEb5GpxxVu_dhnMbb8VgqG6qd1lZKW9sBVrCmBVRX_tZ3IrM_EWzBYFIHNgL80PE85Uj1U5jzfxZVmYbHJN7f9nz0CDSw28GbP0SxcOvG_KuC-3HYwc3grq__1qAAAAATPH6AEA"
BOT_TOKEN = "6093418154:AAGBKB46QCGoVm6C_CKDgcRgAGOfqbogg8k"

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
