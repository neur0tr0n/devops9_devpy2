boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(girls) == len(boys):
    boys_sorted = sorted(boys)
    girl_sorted = sorted(girls)
    print('Идеальные пары:')
    for i in range(0, len(boys) - 1):
        print(f'{boys_sorted[i]} и {girl_sorted[i]}')
else:
    print('Кто-то может остаться без пары!')
