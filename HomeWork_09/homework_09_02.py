import requests
import json
import os

class YaFileUploader:
    _token: str
    _token_file: str
    _headers = {}
    _params = {'fields': 'used_space'}

    def __init__(self, file: str):
        self._token_file = file
        self.load_token()
        self._headers = {'Authorization': f'OAuth {self._token}'}

    def get_token(self):
        return self._token

    def load_token(self):
        with open(self._token_file, 'r') as f:
            data_ = json.load(f)
        self._token = data_['token']

    def upload_file(self, query: str = None):
        url = 'https://cloud-api.yandex.net/v1/disk'
        self._params['fields'] = query
        resp = requests.get(url, headers=self._headers, params=self._params)
        return resp.content


source_dir = 'Files'
token_file = 'authentication.json'
uploader = YaFileUploader(token_file)
response = uploader.upload_file('used_space')
print(response)

