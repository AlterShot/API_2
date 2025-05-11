# Импортируем библиотеки
import datetime
import os

from requests import Response


# Создаем класс для логирования
class Logger():
    # Создаем переменную с путем для сохранения файла
    file_name = f"logs/log_{str(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))}.log"

    # Создаем метод класса для записи лог-файла
    @classmethod
    def write_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf-8') as logger_file:
            logger_file.write(data)

    # Создаем метод для логирования отправленного запроса
    @classmethod
    def add_request(cls, url: str, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = f'\n-----\n'
        data_to_add += f'Test: {test_name}\n'
        data_to_add += f'Time: {str(datetime.datetime.now())}\n'
        data_to_add += f'Request method: {method}\n'
        data_to_add += f'Request url: {url}\n'
        data_to_add += '\n'

        cls.write_to_file(data_to_add)

    # Создаем метод для логирования полученного ответа
    @classmethod
    def add_response(cls, result: Response):
        headers_dict = dict(result.headers)
        cookies_dict = dict(result.cookies)

        data_to_add = f'Response code: {result.status_code}\n'
        data_to_add += f'Response text: {result.text}\n'
        data_to_add += f'Response headers: {headers_dict}\n'
        data_to_add += f'Response cookies: {cookies_dict}\n'
        data_to_add += f'\n-----\n'

        cls.write_to_file(data_to_add)
