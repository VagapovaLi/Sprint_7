import allure
import pytest
import requests
from data import Response
from urls import Urls



@allure.story('Сценарии создания курьера')
class TestCreateCourier:
    @allure.title('Создание курьера с валидными данными.Ожидаемый результат: 201')
    def test_create_courier_success_answer_201(self, create_courier):
        response = create_courier
        assert response.status_code == 201 and response.text == Response.RESPONSE_REGISTRATION_SUCCESSFUL


    @allure.title('Проверка ошибки при создании дублирующей сущности курьера.Ожидаемый результат: 409')
    def test_create_courier_duplicate_login(self, courier_data_login_password):
        requests.post(Urls.URL_courier_create, data=courier_data_login_password)
        response = requests.post(Urls.URL_courier_create, data=courier_data_login_password)
        assert response.status_code == 409 and response.json()["message"] == Response.RESPONSE_LOGIN_USED


    @allure.title('Создание курьера с обязательными полями без имени.Ожидаемый результат: 201')
    def test_create_courier_required_fields_without_name(self,courier_data_without_name):
        response = requests.post(Urls.URL_courier_create, data=courier_data_without_name)
        assert response.status_code == 201 and response.text == Response.RESPONSE_REGISTRATION_SUCCESSFUL


    @allure.title('Создание курьера с существующем логиномю.Ожидаемый результат: 409')
    def test_create_courier_with_existing_login(self,couriers_data_existing_login):
        requests.post(Urls.URL_courier_create, data=couriers_data_existing_login[0])
        response = requests.post(Urls.URL_courier_create, data=couriers_data_existing_login[1])
        assert response.status_code == 409 and response.json()["message"] == Response.RESPONSE_LOGIN_USED


    @allure.title('Проверка ошибки при создании курьера без обязательных полей.Ожидаемый результат: 400')
    @pytest.mark.parametrize('field, empty_value', [('login', ''), ('password', '')])
    def test_create_courier_without_required_fields(self, courier_data_login_password, field, empty_value):
        courier_data_login_password[field] = empty_value
        response = requests.post(Urls.URL_courier_create, data=courier_data_login_password)
        assert response.status_code == 400 and response.json()["message"] == Response.RESPONSE_NO_DATA_ACCOUNT

