# Импортируем библиотеки
from requests import Response

from utils.api import GoogleMapsApi


# Создаем класс для тестов
class TestCreatePlace:

    def test_create_new_place(self):
        # Печатаем, что идет метод POST
        print('POST method')

        # Проводим тест
        post_result: Response = GoogleMapsApi.create_new_place()

        # Добавляем переменную формата json
        post_result_json = post_result.json()

        # Получаем из нее place_id
        place_id = post_result_json.get('place_id')

        # Печатаем, что идет метод GET
        print('GET method')

        # Выполняем метод GET
        get_result: Response = GoogleMapsApi.get_new_place(place_id)
