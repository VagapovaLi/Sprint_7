import pytest
import requests
import helpers
from urls import Urls


@pytest.fixture
def create_courier(courier_data_login_password):
    response = requests.post(Urls.URL_courier_create, json=courier_data_login_password)

    yield response
    # Аутентификация курьера для получения его ID
    login_response = requests.post(Urls.URL_courier_login, json={
        "login": courier_data_login_password["login"],
        "password": courier_data_login_password["password"]
    })

    courier_id = login_response.json()["id"]
    # Удаление курьера после теста
    requests.delete(f"{Urls.URL_courier_create}{courier_id}")

@pytest.fixture
#Генерирует данные курьера со случайным логином, паролем и именем.
def courier_data_login_password():
    data_courier = helpers.CourierDataGenerator()
    return data_courier.generate_random_data_courier()

@pytest.fixture
#Создает курьера только с логином и паролем, без имени.
def courier_data_without_name(courier_data_login_password):
    courier_data_login_password['firstName'] = ''
    return courier_data_login_password


@pytest.fixture
#Создает двух курьеров с одинаковым логином.
def couriers_data_existing_login():
    courier_1 = helpers.CourierDataGenerator()
    courier_2 = helpers.CourierDataGenerator()
    return (
        courier_1.generate_data_courier_static_login(),
        courier_2.generate_data_courier_static_login()
    )



