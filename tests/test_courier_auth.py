import allure
import pytest
import requests
import data
import helpers
from urls import Urls
import json



class TestCourierAuth:

    @allure.title('Проверка успешной авторизации  курьера при заполнении обязательных полей.Ожидаемый результат: 200')
    def test_successful_authorization(self,create_courier):
        response = create_courier
        login_data = json.loads(response.request.body)
        login_data.pop('firstName')
        login_response = requests.post(url=Urls.URL_courier_login, json=login_data)
        assert login_response.status_code == 200
        assert login_response.json()['id'] and isinstance(login_response.json()['id'], int)

    @allure.title('Проверка ошибки при неверном логине или пароле.Ожидаемый результат: 404')
    @pytest.mark.parametrize('field, invalid_value', [('login', helpers.StringGenerator.generate_random_string(10)),
                                                      ('password', helpers.StringGenerator.generate_random_string(10))])
    def test_authorization_invalid_login_password(self,courier_data_without_name,field, invalid_value):
        requests.post(Urls.URL_courier_create, data=courier_data_without_name)
        courier_data_without_name[field] = invalid_value
        login_response = requests.post(Urls.URL_courier_login, data=courier_data_without_name)
        assert login_response.status_code == 404 and login_response.json()[
            "message"] == data.Response.RESPONSE_ACCOUNT_NOT_FOUND

    @allure.title('Проверка ошибки при отсутсвиии одного из обязательных полей.Ожидаемый результат: 400')
    @pytest.mark.parametrize('key, value', [('login', ''), ('password', '')])
    def test_courier_login_empty_credentials_bad_request(self, courier_data_without_name, key, value):
        courier_data_without_name[key] = value
        currier_resp = requests.post(Urls.URL_courier_login, data=courier_data_without_name)
        assert currier_resp.status_code == 400 and currier_resp.json()[
            "message"] == data.Response.RESPONSE_NO_DATA_INPUT
