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

    # Создаем статичный метод для проверки совпадения содержания поля
    @staticmethod
    def check_exact_field_phrase(response: Response, field_name, message):
        field_to_check = response.json()
        msg_to_check = field_to_check.get(field_name)
        assert msg_to_check == message, f"{field_name}\'s message incorrect"
        print(f"{field_name}\'s message correct")

    # Создаем статичный метод для проверки частичного совпадения поля по слову
    @staticmethod
    def check_partial_field_phrase(response: Response, field_name, word):
        field_to_check = response.json()
        word_to_check = field_to_check.get(field_name)
        assert word in word_to_check, f"\'{word}\' is not present in {field_name}"
        print(f"\'{word}\' is present in {field_name}")
