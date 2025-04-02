import datetime

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

class LimitPageOrders:

    #Лимит на страницы заказов:
    limit_page_orders = {
        "limit": "5",
        "page": "0"
    }