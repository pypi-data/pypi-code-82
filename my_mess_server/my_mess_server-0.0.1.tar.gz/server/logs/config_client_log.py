"""Кофнфиг клиентского логгера"""
import sys
import os
import logging
# sys.path.append(os.path.join(os.getcwd(), '..'))


# Текущий уровень логирования
LOGGING_LEVEL = logging.DEBUG

# создаём формировщик логов (formatter):
CLIENT_FORMATTER = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

# Подготовка имени файла для логирования
PATH = os.getcwd()
PATH = os.path.join(PATH, 'client.log')

# создаём потоки вывода логов
STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(CLIENT_FORMATTER)
STREAM_HANDLER.setLevel(logging.ERROR)
LOG_FILE = logging.FileHandler(PATH, encoding='utf8')
LOG_FILE.setFormatter(CLIENT_FORMATTER)

# создаём регистратор и настраиваем его
LOGGER = logging.getLogger('client')
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(LOGGING_LEVEL)

# отладка
if __name__ == '__main__':
    LOGGER.critical('Критическая ошибка')
    LOGGER.error('Ошибка')
    LOGGER.debug('Отладочная информация')
    LOGGER.info('Информационное сообщение')
