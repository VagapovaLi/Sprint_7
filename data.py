import datetime
import allure
import requests
from urls import Urls

class Response:
    #Запрос с несуществующей парой логин-пароль:
    RESPONSE_ACCOUNT_NOT_FOUND = 'Учетная запись не найдена'

    #Запрос без логина или пароля:
    RESPONSE_NO_DATA_INPUT = 'Недостаточно данных для входа'

    #Запрос без логина или пароля:
    RESPONSE_NO_DATA_ACCOUNT = 'Недостаточно данных для создания учетной записи'

    #Запрос с повторяющимся логином:
    RESPONSE_LOGIN_USED = 'Этот логин уже используется. Попробуйте другой.'

    #Успешное создание учетной записи:
    RESPONSE_REGISTRATION_SUCCESSFUL = '{"ok":true}'

class OrderData:
    #Создание заказа
    order_data = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": []
        }


#class LimitPageOrders:

    #Лимит на страницы заказов:
    #limit_page_orders = {
        #"limit": "5",
       # "page": "0"
    #}

