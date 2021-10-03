queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]
stats = {}


def recalc_percent():
    total_sum = 0
    for stat in stats.values():
        total_sum += stat['count']
    if total_sum != 0:
        for stat in stats.values():
            stat['percent'] = round(stat['count'] / total_sum * 100, 2)


for query in queries:
    query_word_count = len(query.split())
    if query_word_count not in stats:
        tmp_d = dict({'count': 1, 'percent': 0.0})
        stats[query_word_count] = tmp_d
        recalc_percent()
    else:
        tmp_d = stats[query_word_count]
        tmp_d['count'] += 1
        stats[query_word_count] = tmp_d
        recalc_percent()
print(stats)
