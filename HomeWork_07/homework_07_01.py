file_name = 'ingredients'

with open(file_name, 'r') as f:
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

print(cook_book)