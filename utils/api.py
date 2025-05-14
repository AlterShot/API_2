# Импортируем класс
from utils.http_methods import HttpMethods

# Создаем нужные переменные
base_url = 'https://rahulshettyacademy.com'
key = '?key=qaclick123'


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

        # Возвращаем значение метода POST
        return post_result

    # Создаем статичный метод GET
    @staticmethod
    def get_new_place(place_id):
        # Собираем url и печатаем его
        get_path = '/maps/api/place/get/json'
        get_url = base_url + get_path + key + "&place_id=" + place_id
        print(f'full GET path: {get_url}')

        # Делаем запрос с кастомным методом GET, печатаем получившийся текст
        get_result = HttpMethods.get(get_url)
        print(get_result.text)

        # Возвращаем значение метода GET
        return get_result

    # Создаем статичный метод PUT
    @staticmethod
    def put_new_place(place_id):

        # Создаем переменную для обновления данных
        put_place_info = {
            "place_id" : place_id,
            "address" : "100 Lenina street, RU",
            "key" : "qaclick123"
        }

        # Собираем url и печатаем его
        put_path = '/maps/api/place/update/json'
        put_url = base_url + put_path + key
        print(f'full PUT path: {put_url}')

        # Вызываем кастомный метод PUT, печатаем получившийся текст
        put_result = HttpMethods.put(put_url, put_place_info)
        print(put_result.text)

        # Возвращаем значение метода PUT
        return put_result

    # Создаем статичный метод DELETE
    @staticmethod
    def delete_new_place(place_id):

        # Создаем переменную для удаления данных
        delete_place_info = {
            "place_id" : place_id
        }

        # Собираем url и печатаем его
        delete_path = '/maps/api/place/delete/json'
        delete_url = base_url + delete_path + key
        print(f'full DELETE path: {delete_url}')

        # Вызываем метод DELETE, печатаем получившийся текст
        delete_result = HttpMethods.delete(delete_url, delete_place_info)
        print(delete_result.text)

        # Возвращаем значение метода DELETE
        return delete_result
