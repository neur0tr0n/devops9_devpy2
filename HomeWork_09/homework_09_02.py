import requests
import json
import os

class YaFileUploader:
    _token: str
    _token_file: str

    def __init__(self, file: str):
        self._token_file = file
        self.load_token()

    def get_token(self):
        return self._token

    def load_token(self):
        with open(self._token_file, 'r') as f:
            data_ = json.load(f)
        self._token = data_['token']

    def upload_file(self, file_path: str):
        return None


source_dir = 'Files'
url = 'https://cloud-api.yandex.net:443'
token_file = 'authentication.json'

uploader = YaFileUploader(token_file)
print(uploader.get_token())

for root, dirs, files in os.walk(source_dir):
    for file in files:
        print(root.join(file))

