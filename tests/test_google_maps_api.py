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

        # Печатаем, что идет метод GET после POST
        print('GET POST method')

        # Выполняем метод GET после POST
        get_result: Response = GoogleMapsApi.get_new_place(place_id)

        # Печатаем, что идет метод PUT
        print('PUT method')

        # Выполняем запрос PUT
        put_result : Response = GoogleMapsApi.put_new_place(place_id)

        # Повторяем метод GET после PUT
        print('GET PUT method')

        # Выполняем метод GET после PUT
        get_result: Response = GoogleMapsApi.get_new_place(place_id)

        # Печатаем, что идет метод DELETE
        print('DELETE method')

        # Выполняем запрос DELETE
        delete_result: Response = GoogleMapsApi.delete_new_place(place_id)

        # Показываем, что снова выполняем GET
        print('GET DELETE method')

        # Проверяем, удалилась ли локация с помощью GET
        get_result: Response = GoogleMapsApi.get_new_place(place_id)
