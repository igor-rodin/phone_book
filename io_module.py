# Процедуры работы с базой данных

import settings
import json
import os


def load_db() -> list:  # читаем из файла json в список словарей
    if os.path.isfile(settings.DB_FILE):
        with open(settings.DB_FILE, 'r', encoding='UTF-8') as f:
            ret = json.load(f)
        return ret
    else:
        return []


def save_db(local_list: list):  # пишем в файл json список словарей
    if len(local_list) > 0:
        with open(settings.DB_FILE, 'w', encoding='UTF-8') as f:
            json.dump(local_list, f)
