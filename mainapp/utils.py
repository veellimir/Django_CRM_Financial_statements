import os


from dotenv import load_dotenv
import requests

from .forms import OperationsForm

load_dotenv()


URL = 'https://api.fintablo.ru/v1/'
TOKEN = os.getenv('API_KEY_FIN-TABLO')
HEADERS = {'Authorization': f'Bearer {TOKEN}'}


def get_list_money():
    """
    Получение списка счётов пользователей
    :return: id пользователей на страницу регистрации
    """
    url_pattern = URL + 'moneybag'

    response = requests.get(url_pattern, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        user_info = [{'id': item['id'], 'name': item['name']} for item in data['items']]

        print('\nСписок счётов пользователей\n', user_info)
        return user_info
    else:
        print(f"Ошибка при получении данных: {response.status_code}")


def get_list_data(endpoint):
    """
    Динамическая функция получение списка данных по API
    :param endpoint: точка параметра запроса
    :return: Список данных
    """
    url_pattern = URL + endpoint
    response = requests.get(url_pattern, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()

        # print('\nСделки и парнтёры\n', data)
        return [item['name'] for item in data['items']]

    print(f"Ошибка при получении данных: {response.status_code}")
    return False


def get_list_deal_id():
    return get_list_data('deal')


def get_list_counterparty():
    # return get_list_data('partner')
    """
        Получение списка счётов пользователей
        :return: id пользователей на страницу регистрации
        """
    url_pattern = URL + 'partner'

    response = requests.get(url_pattern, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        user_info = [{'id': item['id'], 'name': item['name']} for item in data['items']]

        print('\nСписок счётов пользователей\n', user_info)
        return user_info
    else:
        print(f"Ошибка при получении данных: {response.status_code}")


def get_list_articles():
    """
    Получение списка счётов пользователей
    :return: id пользователей на страницу регистрации
    """
    url_pattern = URL + 'category'

    response = requests.get(url_pattern, headers=HEADERS)
    if response.status_code == 200:
        data = response.json()
        user_info = [{'id': item['id'], 'name': item['name']} for item in data['items']]

        # print('\nСписок статьей\n', data)
        return data
    else:
        print(f"Ошибка при получении данных: {response.status_code}")


def add_outcome(form, moneybag_id):
    """
    Функция добавления отчёта по API
    :return:
    """
    url_pattern = URL + 'transaction'

    payload = {
        "value": form.cleaned_data['value'],
        "moneybagId": moneybag_id,
        "group": "outcome",
        "description": form.cleaned_data['description'],
        "partnerId": form.cleaned_data['counterparty'],
        "date": "10.04.2024",
        "categoryId": "",
        # "categoryId": form_data['reports']
    }
    print(payload)
    response = requests.post(url_pattern, json=payload, headers=HEADERS)

    if response.status_code == 200:
        print('Операция добавлена')
    else:
        print('Ошибка !!!', response.text)
