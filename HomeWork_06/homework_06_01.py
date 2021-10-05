class Animals(object):
    name = ''
    weight = 0.0

    def sounds(self):
        NotImplementedError('Необходимо определить метод')

    def feed(self):
        NotImplementedError('Необходимо определить метод')

    def harverst(self):
        NotImplementedError('Необходимо определить метод')


class Mammals(Animals):
    def sounds(self):
        NotImplementedError('Необходимо определить метод')

    def feed(self):
        return 'ем траву'

    def harverst(self):
        NotImplementedError('Необходимо определить метод')


class Birds(Animals):
    def sounds(self):
        NotImplementedError('Необходимо определить метод')

    def feed(self):
        return 'ем зерно'

    def harverst(self):
        NotImplementedError('Необходимо определить метод')


class Goose(Birds):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def sounds(self):
        return 'га-га-га'

    def harverst(self):
        return 'гусиные яйца'


class Duck(Birds):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def sounds(self):
        return 'кря-кря-кря'

    def harverst(self):
        return 'утиные яйца'


class Chicken(Birds):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def sounds(self):
        return 'кудах-тах-тах'

    def harverst(self):
        return 'куриные яйца'


class Cow(Mammals):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def sounds(self):
        return 'му-муууу'

    def harverst(self):
        return 'коровье молоко'


class Goat(Mammals):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def sounds(self):
        return 'ме-е-е-е'

    def harverst(self):
        return 'козье молоко'


class Sheep(Mammals):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def sounds(self):
        return 'бе-е-е-е'

    def harverst(self):
        return 'овечья шерсть'


goose1 = Goose('Белый', 5)
goose2 = Goose('Серый', 6)
cow = Cow('Манька', 200)
sheep1 = Sheep('Барашек', 40)
sheep2 = Sheep('Кудрявый', 45)
chicken1 = Chicken('Ко-Ко', 2)
chicken2 = Chicken('Кукареку', 3)
goat1 = Goat('Рога', 30)
goat2 = Goat('Копыта', 35)
duck = Duck('Копыта', 4)

animal_list = [goose1, goose2, cow, sheep1, sheep2, chicken1, chicken2, goat1, goat2, duck]

for animal in animal_list:
    print(f'Я {animal.name} звучу как "{animal.sounds()}". Я {animal.feed()} и даю {animal.harverst()}.')

total_weight = 0
for animal in animal_list:
    total_weight += animal.weight
print(f'Общий вес всех животных: {total_weight}')

heaviest_animal_weight = 0
heaviest_animal_name = ''
for animal in animal_list:
    if animal.weight > heaviest_animal_weight:
        heaviest_animal_name = animal.name
        heaviest_animal_weight = animal.weight
print(f'Самое тяжелое животное: {heaviest_animal_name} с весом {heaviest_animal_weight}')







