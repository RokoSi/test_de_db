import logging
import os
from pprint import pprint

from consumer import mgs_kafka_json
from json_parsing import pars_user
from settings import settings
from db_use import save_user
from db_use.data_provider import create_db

log_dir = os.path.join(os.getcwd(), "logs")
log_file = os.path.join(log_dir, "logfile.log")
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    filename=log_file,
    filemode="a",
    encoding="utf-8",
    level=logging.INFO,
    format="'%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %I:%M:%S %p",
)
log = logging.getLogger(__name__)


def main():
    # import os
    # file_name = '.env.dev'
    # directories = ['.', '..', '../src']
    # for directory in directories:
    #     file_path = os.path.join(directory, file_name)
    #     if os.path.isfile(file_path):
    #         print(f"Файл найден: {file_path}")
    #         break
    # else:
    #     print(f"Файл {file_name} не найден в указанных директориях.")


    print("создание базы данных")
    if create_db(settings):
        print("База данных не создана")

    users = mgs_kafka_json()
    for data in users:

        if data:
            data = list([data])

            user = pars_user(data)
            if save_user(settings, user[0]):
                print("пользователь добавлен в бд1")
                log.info("пользователь добавлен в бд2")
            else:
                print("пользователь не добавлен в бд3")
                log.info("пользователь не добавлен в бд4")


if __name__ == "__main__":
    main()
