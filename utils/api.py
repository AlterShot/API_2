# Импортируем класс
from utils.http_methods import HttpMethods

# Создаем нужные переменные
base_url = 'https://rahulshettyacademy.com'
key = '&key=qaclick123'


# Создаем класс
class GoogleMapsApi():

    # Создаем статичный метод для создания новой локации
    @staticmethod
    def create_new_place():
        # Создаем переменную с информацией о новом месте
        new_place_info = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        # Указывает путь к API и собираем url, перчатаем его
        post_path = '/maps/api/place/add/json'
        post_url = base_url + post_path + key
        print(f'full POST path: {post_url}')

        # Делаем запрос с кастомным методом POST, печатаем получившийся текст
        post_result = HttpMethods.post(post_url, new_place_info)
        print(post_result.text)

        # Возвращаем значение
        return post_result
