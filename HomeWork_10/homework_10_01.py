import json
import time
import requests


class VKUser:
    _friends: list
    _token: str
    _user_id: int
    _app_id: int
    _params1: dict
    _params2: dict
    _page_url: str

    def __init__(self, appid: int = None, userid: int = None):
        self._app_id = appid
        self._user_id = userid
        self.get_token('token.json')
        self._page_url = 'https://vk.com/id' + str(userid)

    def get_token(self, file):
        with open(file, 'r') as f:
            data = json.load(f)
        self._token = data['access_token']

    def authorize(self):
        self._params1 = {
            'client_id': self._app_id,
            'redirect_uri': None,
            'display': 'page',
            'scope': ['friends'],
            'response_type': 'token',
            'v': '5.131'
        }
        url = 'https://oauth.vk.com/authorize'
        resp = requests.get(url, params=self._params1)
        return resp.url

    def get_mutual_friends(self, friend: int = None):
        url = 'https://api.vk.com/method/friends.getMutual'
        self._params2 = {
            'source_uid': self._user_id,
            'target_uid': friend,
            'access_token': self._token,
            'v': '5.131'
        }
        resp = requests.get(url, params=self._params2).json()
        return resp['response']

    def get_users_info(self, userid: int = None):
        fio = ''
        url = 'https://api.vk.com/method/users.get'
        self._params2 = {
            'user_id': self._user_id,
            'fields': 'site',
            'access_token': self._token,
            'v': '5.131'
        }
        resp = requests.get(url, params=self._params2).json()
        list_params = resp['response']
        for param in list_params:
            fio = f'{param["last_name"]} {param["first_name"]}'
        return fio

    def get_friends(self, userid: int = None):
        url = 'https://api.vk.com/method/friends.get'
        self._params2 = {
            'user_id': self._user_id,
            'access_token': self._token,
            'v': '5.131'
        }
        resp = requests.get(url, params=self._params2).json()
        return resp['response']['items']

    def get_profile_url(self, userid: int = None):
        return self._page_url


app_id = 7977638
# user_id = 681170666
# user1 = VKUser(appid=app_id, userid=user_id)
# print(user1.authorize())

user_id = 140591265
user_friend_id = 20386970
user = VKUser(appid=app_id, userid=user_id)
user_friend = VKUser(appid=app_id, userid=user_friend_id)
print(user.get_users_info())
print(user_friend.get_users_info())
mutual_friends = user.get_mutual_friends(user_friend_id)
print('Mutual friends:')
users_list: list = []
for friend_ in mutual_friends:
    users_list.append(VKUser(appid=app_id, userid=friend_))

for usr in users_list:
    print(f'{usr.get_users_info()} ({usr.get_profile_url()})')
    time.sleep(0.4)


