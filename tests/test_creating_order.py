import pytest
import allure
import requests
import json
from urls import Urls
from data import OrderData


class TestOrderCreation:
    @allure.title("Создания заказа с возможностью выбора одного цвета, обоих цветов или без указания цвета")
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []])
    def test_creating_order_wit_choice_color(self,color):
        data = OrderData.order_data
        data['color'] = color
        data_json = json.dumps(data)
        response = requests.post(Urls.URL_orders_create, data=data_json)
        response_json = response.json()
        assert response.status_code == 201 and 'track' in response_json.keys()


