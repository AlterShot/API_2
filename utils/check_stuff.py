# Импортируем библиотеку
import json

from requests import Response


# Создаем класс для проверок
class CheckStuff:

    # Создаем статичный метод для проверки статус-кода
    @staticmethod
    def status_code_check(response: Response, status_code):
        assert response.status_code == status_code, (f"Error. Status code is {response.status_code}"
                                                     f"Must be {status_code}")
        print(f"Correct. Status code is {status_code}")


    # Создаем статичный метод для проверки наличия обязательных полей
    @staticmethod
    def json_token_check(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value, "Some field not present"
        print("Every field present")
