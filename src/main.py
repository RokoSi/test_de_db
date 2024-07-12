import logging
import os

from consumer import mgs_kafka_json
from db_use import save_user
from json_parsing import pars_user
from settings import settings

log = logging.getLogger(__name__)

log_dir = os.path.join(os.getcwd(), "logs")
log_file = os.path.join(log_dir, "logfile.log")
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    filename=log_file,
    filemode="a",
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s - %(message)s",
    datefmt="%d/%m/%Y %I:%M:%S %p",
)


def main():
    for data in mgs_kafka_json():
        if data:
            user = pars_user(data)
            if save_user(settings, user[0]):
                print("пользователь добавлен в бд")
            else:
                print("пользователь не добавлен в бд")


if __name__ == "__main__":
    main()
