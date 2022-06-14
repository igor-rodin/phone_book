# Функционал работы с журналом

import time
import settings


def add2log(text):  # пишем все в лог - файл
    with open(settings.LOG_FILE, 'a', encoding='UTF-8') as f:
        f.write(
            f'{time.strftime("%Y.%m.%d %H:%M:%S",time.gmtime(time.time()))},{text}\n')
