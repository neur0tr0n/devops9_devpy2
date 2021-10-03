stats = {'facebook': 55,
         'yandex': 120,
         'vk': 115,
         'google': 99,
         'email': 42,
         'ok': 98
         }
most_popular = ''
prev_rating = 0
for channel, stat in stats.items():
    if stat > prev_rating:
        prev_rating = stat
        most_popular = channel

print(f'Самый популярный канал: {most_popular.capitalize()} с объемом {stats[most_popular]}')