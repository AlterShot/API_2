# Импортируем библиотеку
import requests

# Импортируем класс логирования
from utils.logger import Logger


# Создаем общий класс
class HttpMethods:
    # Добавляем headers и cookie
    headers = {'Content-type': 'application/json'}
    cookies = ""

    # Создаем статичный метод для get-запроса, добавляем к нему логирование
    @staticmethod
    def get(url):
        Logger.add_request(url, method='GET')
        result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookies)
        Logger.add_response(result)
        return result

    # Создаем статичный метод для post-запроса, добавляем к нему логирование
    @staticmethod
    def post(url, body):
        Logger.add_request(url, method='POST')
        result = requests.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookies)
        Logger.add_response(result)
        return result

    # Создаем статичный метод для put-запроса, добавляем к нему логирование
    @staticmethod
    def put(url, body):
        Logger.add_request(url, method='PUT')
        result = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookies)
        Logger.add_response(result)
        return result

    # Создаем статичный метод для delete-запроса, добавляем к нему логирование
    @staticmethod
    def delete(url, body):
        Logger.add_request(url, method='DELETE')
        result = requests.delete(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookies)
        Logger.add_response(result)
        return result
