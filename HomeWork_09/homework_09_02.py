import requests
import json
import os

class YaFileUploader:
    _token: str
    _token_file: str
    _headers = {}
    _params = {}

    def __init__(self, file: str):
        self._token_file = file
        self.load_token()
        self._headers['Authorization'] = f'OAuth {self._token}'
        self._headers['Accept'] = 'application/json'

    def get_token(self):
        return self._token

    def load_token(self):
        with open(self._token_file, 'r') as f:
            data_ = json.load(f)
        self._token = data_['token']

    def upload_file(self, file_path: str = None):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        self._params['path'] = file_path
        self._params['overwrite'] = 'True'
        resp = requests.get(url, headers=self._headers, params=self._params).json()
        href = resp['href']
        with open(file_path, 'rb') as f:
            reps: requests = requests.post(href, files={'file': file_path})
        return reps.status_code


source_dir = 'Files'
token_file = 'authentication.json'
uploader = YaFileUploader(token_file)
response = uploader.upload_file('newsafr.xml')
if response == 201:
    print(f'({response}) Created')
else:
    print(f'({response}) Something gone wrong!')


