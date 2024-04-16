import os
import requests

API_YANDEX_DISK = 'y0_AgAAAAAS_BYtAADLWwAAAAD_adbvAABxjkOWeDVHErJGw2jECuPYiXSKKA'


def disk_resources_upload(file_path, dir_path=''):
    params = {
        'path': os.path.join(dir_path, os.path.basename(file_path)),
        'overwrite': 'true'
    }
    url_query = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    result_query = send_query_ya_disk(url_query, params)

    if 'error' not in result_query:
        with open(file_path, 'rb') as f:
            files = {'file': f}
            response_upload = requests.put(result_query['href'], files=files)
            http_code = response_upload.status_code
        return http_code
    else:
        return result_query['message']


def send_query_ya_disk(url, params):
    response = requests.get(url, params=params, headers={'Authorization': f'OAuth {API_YANDEX_DISK}'})
    return response.json() if response.ok else {'error': 'Failed to get upload URL'}


# Пример использования функции
file_path = './media/Снимок_экрана_от_2024-04-16_12-28-48.png'
dir_path = '/reports'
response_code = disk_resources_upload(file_path, dir_path)
print(response_code)
