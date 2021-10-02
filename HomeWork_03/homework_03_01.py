boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']


if len(girls) == len(boys):
    boys_sorted = sorted(boys)
    girl_sorted = sorted(girls)
    pairs = zip(boys_sorted, girl_sorted)
    print('Идеальные пары:')
    for pair in pairs:
        print(f'{pair[0]} и {pair[1]}')
else:
    print('Кто-то может остаться без пары!')
