import os

import requests
from dotenv import load_dotenv

from django.contrib import messages
from django.db.models import Q

from .models import Operations

load_dotenv()

FIN_TABLO_URL = 'https://api.fintablo.ru/v1/'
FIN_TABLO_TOKEN = os.getenv('API_KEY_FIN_TABLO')
HEADERS_FIN_TABLO = {'Authorization': f'Bearer {FIN_TABLO_TOKEN}'}

URL_YANDEX = 'https://cloud-api.yandex.net/v1/disk/resources'
YANDEX_TOKEN = os.getenv('API_YANDEX_DISK')
HEADERS_YANDEX = {'Authorization': f'OAuth {YANDEX_TOKEN}'}


# REQUEST GET LIST
def get_data_from_api(endpoint):
    """
    Динамическая функция для получения списков
    :param endpoint:
    :return: moneybag, deal, partner, category
    """
    url_pattern = FIN_TABLO_URL + endpoint
    response = requests.get(url_pattern, headers=HEADERS_FIN_TABLO)

    if response.status_code == 200:
        data = response.json()
        return [{'id': item['id'], 'name': item['name']} for item in data['items']]
    else:
        print(f"Ошибка при получении данных: {response.status_code}")


def get_list_money():
    return get_data_from_api('moneybag')


# print(get_list_money())


def get_list_deal():
    return get_data_from_api('deal')


def get_list_counterparty():
    return get_data_from_api('partner')


def get_list_articles():
    return get_data_from_api('category')


# ======================================================================================================================
# REQUEST POST
def add_outcome(request, form, moneybag_id, description, during_period):
    """
    Функция отправки данных в ФинТабло
    :param request:
    :param form:
    :param moneybag_id:
    :param description:
    :param during_period:
    :return: post send api:
    """
    during_period_str = during_period.strftime('%d.%m.%Y')

    payload = {
        "value": form.cleaned_data['value'],
        "moneybagId": moneybag_id,
        "group": "outcome",
        "description": description,
        "date": during_period_str,
    }
    if form.cleaned_data.get('undisclosed'):
        payload["categoryId"] = form.cleaned_data['undisclosed']

    if form.cleaned_data.get('deal_name'):
        payload["dealId"] = form.cleaned_data['deal_name']

    if form.cleaned_data.get('selectedDealCounterparty'):
        payload["partnerId"] = form.cleaned_data['counterparty']

    url_pattern = FIN_TABLO_URL + 'transaction'
    print(payload)
    try:
        response = requests.post(url_pattern, json=payload, headers=HEADERS_FIN_TABLO)
        response.raise_for_status()
        print('Операция добавлена')

    except requests.exceptions.RequestException as e:
        print('Произошла ошибка при выполнении запроса:', e)
        messages.error(request, 'Произошла ошибка при выполнении запроса. Пожалуйста, попробуйте еще раз.')


def disk_resources_upload(file_path, name_image, dir_path):
    """
    Функция загрузки изображения на Я-Диск
    :param file_path:
    :param name_image:
    :param dir_path:
    :return: put send api:
    """
    params = {
        'path': os.path.join(dir_path, os.path.basename(name_image)),
        'overwrite': 'true'
    }
    url_query = URL_YANDEX + '/upload'
    result_query = send_query_ya_disk(url_query, params)

    if 'error' not in result_query:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            response_upload = requests.put(result_query['href'], files=files)
            http_code = response_upload.status_code

        return http_code
    else:
        return result_query['error']


def send_query_ya_disk(url, params):
    response = requests.get(url, params=params, headers={'Authorization': f'OAuth {YANDEX_TOKEN}'})
    return response.json() if response.ok else {'error': 'Не удалось получить URL-адрес для загрузки'}


# GET YANDEX_DISK FILES
# def get_files_yandex_disk():
#     url_query = URL_YANDEX + '/last-uploaded'
#
#     try:
#         response = requests.get(url_query, headers=HEADERS_YANDEX)
#         response.raise_for_status()
#         data = response.json()
#
#         print('file', data)
#         return data
#     except requests.exceptions.RequestException as e:
#         print(f"Произошла ошибка при запросе к Яндекс.Диску: {e}")
#         return None


# PUT FOLDER YEAR TO YANDEX_DISK
# def create_year_folder(folder_name):
#     try:
#         current_year = datetime.datetime.now().year
#         folder_path_with_year = os.path.join(folder_name + str(current_year))
#
#         url_query = f'{URL_YANDEX}'
#         folder_path = {'path': folder_path_with_year}
#
#         response = requests.put(url_query, headers=HEADERS_YANDEX, params=folder_path)
#         print(f'{folder_path} статус код: ', response.status_code)
#
#     except Exception as e:
#         print(f"Произошла ошибка: {e}")


# create_year_folder('reports/')

def admin_search_reports(request):
    """
    Функция поиска отчётов
    :param request:
    :return: Отчёт
    """
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

        data_operations = Operations.objects.distinct().filter(
            Q(deal_name__icontains=search_query.lower()) |
            Q(value__icontains=search_query) |
            Q(description__icontains=search_query.lower()) |
            Q(user__first_name__icontains=search_query) |
            Q(during_period__icontains=search_query)
        )
    else:
        data_operations = Operations.objects.all()
    return search_query, data_operations

