# Импортируем библиотеки
from requests import Response

from utils.api import GoogleMapsApi
from utils.check_stuff import CheckStuff


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
        CheckStuff.status_code_check(post_result, 200)

        # Проверяем наличие всех обязательных полей запроса POST
        CheckStuff.json_token_check(post_result, ['status', 'place_id', 'scope', 'reference', 'id'])

        # Проверяем точное совпадение по полю метода POST
        CheckStuff.check_exact_field_phrase(post_result, 'status', 'OK')

        # Печатаем, что идет метод GET после POST
        print('GET POST method')

        # Выполняем метод GET после POST
        get_result: Response = GoogleMapsApi.get_new_place(place_id)

        # Проверяем статус-код запроса GET после POST
        CheckStuff.status_code_check(get_result, 200)

        # Проверяем наличие всех обязательных полей запроса GET после POST
        CheckStuff.json_token_check(get_result, ['location', 'accuracy', 'name',
                                                 'phone_number', 'address', 'types', 'website', 'language'])

        # Проверяем совпадение поля адреса в методе GET
        CheckStuff.check_exact_field_phrase(get_result, 'address', '29, side layout, cohen 09')

        # Печатаем, что идет метод PUT
        print('PUT method')

        # Выполняем запрос PUT
        put_result: Response = GoogleMapsApi.put_new_place(place_id)

        # Проверяем статус-код запроса PUT
        CheckStuff.status_code_check(put_result, 200)

        # Проверяем наличие всех обязательных полей запроса PUT
        CheckStuff.json_token_check(put_result, ['msg'])

        # Проверяем корректность статуса в методе PUT
        CheckStuff.check_exact_field_phrase(put_result, 'msg', 'Address successfully updated')

        # Повторяем метод GET после PUT
        print('GET PUT method')

        # Выполняем метод GET после PUT
        get_result: Response = GoogleMapsApi.get_new_place(place_id)

        # Проверяем статус-код запроса GET после PUT
        CheckStuff.status_code_check(get_result, 200)

        # Проверяем наличие всех обязательных полей запроса GET после PUT
        CheckStuff.json_token_check(get_result, ['location', 'accuracy', 'name',
                                                 'phone_number', 'address', 'types', 'website', 'language'])

        # Проверяем совпадение поля обновленного адреса в методе GET после PUT
        CheckStuff.check_exact_field_phrase(get_result, 'address', '100 Lenina street, RU')

        # Печатаем, что идет метод DELETE
        print('DELETE method')

        # Выполняем запрос DELETE
        delete_result: Response = GoogleMapsApi.delete_new_place(place_id)

        # Проверяем статус-код запроса DELETE
        CheckStuff.status_code_check(delete_result, 200)

        # Проверяем наличие всех обязательных полей запроса DELETE
        CheckStuff.json_token_check(delete_result, ['status'])

        # Проверяем корректность сообщения в методе DELETE
        CheckStuff.check_exact_field_phrase(delete_result, 'status', 'OK')

        # Показываем, что снова выполняем GET
        print('GET DELETE method')

        # Проверяем, удалилась ли локация с помощью GET
        get_result: Response = GoogleMapsApi.get_new_place(place_id)

        # Проверяем статус-код запроса GET после DELETE
        CheckStuff.status_code_check(get_result, 404)

        # Проверяем наличие всех обязательных полей запроса GET после DELETE
        CheckStuff.json_token_check(get_result, ['msg'])

        # Проверяем на наличие слова в методе GET после DELETE
        CheckStuff.check_partial_field_phrase(get_result, 'msg', 'failed')

        # Печатаем, что все тесты прошли успешно
        print("new location creation, refreshing and deleting testing is successful")
