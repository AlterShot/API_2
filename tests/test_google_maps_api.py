# Импортируем библиотеки
from requests import Response

from utils.api import GoogleMapsApi
from utils.status_code import StatusCodeChecking


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

        # Проверяем статус-код запроса POST
        StatusCodeChecking.status_code_check(post_result, 200)

        # Печатаем, что идет метод GET после POST
        print('GET POST method')

        # Выполняем метод GET после POST
        get_result: Response = GoogleMapsApi.get_new_place(place_id)

        # Проверяем статус-код запроса GET после POST
        StatusCodeChecking.status_code_check(get_result, 200)

        # Печатаем, что идет метод PUT
        print('PUT method')

        # Выполняем запрос PUT
        put_result: Response = GoogleMapsApi.put_new_place(place_id)

        # Проверяем статус-код запроса PUT
        StatusCodeChecking.status_code_check(put_result, 200)

        # Повторяем метод GET после PUT
        print('GET PUT method')

        # Выполняем метод GET после PUT
        get_result: Response = GoogleMapsApi.get_new_place(place_id)

        # Проверяем статус-код запроса GET после PUT
        StatusCodeChecking.status_code_check(get_result, 200)

        # Печатаем, что идет метод DELETE
        print('DELETE method')

        # Выполняем запрос DELETE
        delete_result: Response = GoogleMapsApi.delete_new_place(place_id)

        # Проверяем статус-код запроса DELETE
        StatusCodeChecking.status_code_check(delete_result, 200)

        # Показываем, что снова выполняем GET
        print('GET DELETE method')

        # Проверяем, удалилась ли локация с помощью GET
        get_result: Response = GoogleMapsApi.get_new_place(place_id)

        # Проверяем статус-код запроса GET после DELETE
        StatusCodeChecking.status_code_check(get_result, 404)
