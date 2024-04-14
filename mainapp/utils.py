import os
import requests
from dotenv import load_dotenv


load_dotenv()

URL = 'https://api.fintablo.ru/v1/'
TOKEN = os.getenv('API_KEY_FIN-TABLO')
HEADERS = {'Authorization': f'Bearer {TOKEN}'}


# REQUEST GET LIST
def get_data_from_api(endpoint):
    """
    Динамическая функция для получения
    :param endpoint:
    :return: moneybag, deal, partner, category
    """
    url_pattern = URL + endpoint
    response = requests.get(url_pattern, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()

        # print(data)
        return [{'id': item['id'], 'name': item['name']} for item in data['items']]
    else:
        print(f"Ошибка при получении данных: {response.status_code}")


def get_list_money():
    return get_data_from_api('moneybag')


print(get_list_money())


def get_list_deal():
    return get_data_from_api('deal')


# print(get_list_deal())


def get_list_counterparty():
    return get_data_from_api('partner')


def get_list_articles():
    return get_data_from_api('category')


# print(get_list_articles())


# ======================================================================================================================
# REQUEST POST
def add_outcome(form, moneybag_id, description):
    payload = {
        "value": form.cleaned_data['value'],
        "moneybagId": moneybag_id,
        "group": "outcome",
        # "description": form.cleaned_data['description'],
        "description": description,
        # "partnerId": form.cleaned_data['counterparty'],
        "date": "14.04.2024",
        # "categoryId": form.cleaned_data['undisclosed'],
        # "dealId": form.cleaned_data['deal_name'],
    }
    if form.cleaned_data.get('undisclosed'):
        payload["categoryId"] = form.cleaned_data['undisclosed']

    if form.cleaned_data.get('deal_name'):
        payload["dealId"] = form.cleaned_data['deal_name']

    if form.cleaned_data.get('counterparty'):
        payload["partnerId"] = form.cleaned_data['counterparty']

    url_pattern = URL + 'transaction'
    print(payload)
    try:
        response = requests.post(url_pattern, json=payload, headers=HEADERS)
        response.raise_for_status()
        print('Операция добавлена')

    except requests.exceptions.RequestException as e:
        print('Произошла ошибка при выполнении запроса:', e)