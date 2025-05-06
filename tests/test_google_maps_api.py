# Импортируем библиотеки
from requests import Response

from utils.api import GoogleMapsApi


# Создаем класс для тестов
class TestCreatePlace():
    # Печатаем, что идет метод POST
    print('POST method')

    # Проводим тест
    post_result: Response = GoogleMapsApi.create_new_place()
