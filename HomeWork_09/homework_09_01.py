import requests

PARAMS = ''
heroes = ['Hulk', 'Captain America', 'Thanos']
heroes_power = {}
url = 'https://superheroapi.com/api/2619421814940190/search/'
for hero in heroes:
    dict_ = {}
    resp = requests.get(url + hero)
    if resp.status_code == 200:
        hero_intelligence = resp.json()
        iq = hero_intelligence['results'][0]['powerstats']['intelligence']
        dict_ = {'intelligence': iq}
        heroes_power[hero] = dict_

hero_iq = 0
smartest_hero = ''
for hero, iq in heroes_power.items():
    if hero_iq <= int(iq['intelligence']):
        hero_iq = int(iq['intelligence'])
        smartest_hero = hero

print(f'The most smart super hero is {smartest_hero}.')




