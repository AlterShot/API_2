# Импортируем библиотеку
from requests import Response


# Создаем класс для проверки статус-кода
class StatusCodeChecking:

    # Создаем статичный метод для проверки
    @staticmethod
    def status_code_check(response: Response, status_code):
        assert response.status_code == status_code, (f"Error. Status code is {response.status_code}"
                                                     f"Must be {status_code}")
        print(f"Correct. Status code is {status_code}")
