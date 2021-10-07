def get_dict_from_file(file_name_):
    '''
    Функция считывающая словать рецептов из файла
    :param file_name_: Имя файла
    :return: Словарь блюд и их ингредиентов
    '''
    with open(file_name_, 'r') as f:
        lines = f.readlines()

    cook_book = {}
    ingredient_list = []
    ingredient_num = 0
    for line in lines:
        str_ = line.strip()
        if str_.isnumeric():
            ingredient_num = int(str_)
        elif str_.count('|') == 0 and str_.isnumeric() is False and str_ != '':
            dish = str_
        else:
            if ingredient_num > 0:
                ingredient_dict = {}
                ingredient = str_.split('|')
                ingredient_dict['ingredient_name'] = ingredient[0].strip()
                ingredient_dict['quantity'] = int(ingredient[1].strip())
                ingredient_dict['measure'] = ingredient[2].strip()
                ingredient_list.append(ingredient_dict)
                ingredient_num -= 1
        if ingredient_num == 0 and ingredient_list != []:
            cook_book[dish] = ingredient_list.copy()
            ingredient_list.clear()
    return cook_book


def get_shop_list_by_dishes(dishes_, pers_count_=1):
    '''
    Функция? подсчитывающая количество ингредиентов в зависимости
    от выбранных блюд и количества персон
    :param dishes_: Названия блюд
    :param pers_count_: Число персон
    :return: Словарь с необходимыми ингредиентами и их количеством
    '''
    cook_book = get_dict_from_file('ingredients')
    ingredients = {}
    for dish_ in dishes_:
        for ingredient in cook_book[dish_]:
            tmp_dict = {}
            if ingredient['ingredient_name'] in ingredients.keys():
                ingredients[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * pers_count_
            else:
                tmp_dict['measure'] = ingredient['measure']
                tmp_dict['quantity'] = ingredient['quantity'] * pers_count_
                ingredients[ingredient['ingredient_name']] = tmp_dict
    return ingredients


dishes = ['Омлет', 'Фахитос']
print(get_shop_list_by_dishes(dishes, 5))


