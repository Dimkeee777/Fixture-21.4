import json
import requests
import pytest
from datetime import datetime
#
# @pytest.fixture()
# def some_data():
#     return 42
#
# def test_some_data(some_data):
#     assert some_data == 42
#
# @pytest.fixture()
# def get_key():
#     response = requests.post(url='https://petfriends.skillfactory.ru/login',
#                              data={'email': "lbtumatym@gmail.com", 'pass': "dsdsdsawd"})
#     assert response.status_code == 200, 'Запрос выполнен неуспешно'
#     assert 'Cookie' in response.request.headers, 'В запросе не передан ключ авторизации'
#     return response.request.headers.get ('Cookie')
#
# def test_getAllPets(get_key):
#     response = requests.get(url='https://petfriends.skillfactory.ru/api/pets',
#                             headers={"Cookie": get_key})
#     assert response.status_code == 200, 'Запрос выполнен неуспешно'
#     assert len(response.json().get('pets')) > 0, 'Количество питомцев не соответствует ожиданиям'
#
# @pytest.fixture(autouse=True)
# def time_delta():
#     start_time = datetime.now()
#     yield
#     end_time = datetime.now()
#     print (f'\nТест шел: {end_time - start_time}')

# @pytest.fixture(scope='session', autouse=True)
# def class_fixture():
#     print('\nsession fixture starts')
#
# @pytest.fixture(scope='function', autouse=True)
# def function_fixture():
#     print('\nfunction fixture starts')
#
class TestClassScope:

    def test_scope_first(self):
        pass

    def test_scope_second(self):
        pass


@pytest.fixture()
def request_fixture(request):
    print(request.fixturename)
    print(request.scope)
    print(request.function.__name__)
    print(request.cls)
    print(request.module.__name__)
    print(request.fspath)
    if request.cls:
        return f"\n У теста {request.function.__name__} класс есть\n"
    else:
        return f"\n У теста {request.function.__name__} класса нет\n"


def test_request_1(request_fixture):
    print(request_fixture)
    print(request.scope)


class TestClassRequest:

    def test_request_2(self, request_fixture):
        print(request_fixture)