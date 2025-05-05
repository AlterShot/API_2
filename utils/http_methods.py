# Импортируем библиотеку
import requests


# Создаем общий класс
class HttpMethods:
    # Добавляем headers и cookie
    headers = {'Content-type': 'application/json'}
    cookie = ""

    # Создаем статичный метод для get-запроса
    @staticmethod
    def get(url):
        result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result

    # Создаем статичный метод для post-запроса
    @staticmethod
    def post(url, body):
        result = requests.post(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result

    # Создаем статичный метод для put-запроса
    @staticmethod
    def put(url, body):
        result = requests.put(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result

    # Создаем статичный метод для delete-запроса
    @staticmethod
    def delete(url, body):
        result = requests.delete(url, json=body, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result
