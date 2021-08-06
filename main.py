import pprint
pp = pprint.PrettyPrinter(indent=2)
import os
file_path = os.path.join(os.getcwd(), 'recipes.txt')
def get_recipes(file_name):
    """Функция чтения файла + создание словаря нужного формата"""
    cook_dict = {}
    with open(file_name, encoding='utf-8') as file_work:
        f = file_work.read().splitlines()
        i = 0
        while i < len(f):
            dish = f[i]
            ingr_count = int(f[i + 1])
            ingr = []
            for j in range(ingr_count):
                temp_dict = {}
                temp_dict['ingredient_name'] = f[i + 2].split('|')[0]
                temp_dict['quantity'] = int(f[i + 2].split('|')[1])
                temp_dict['measure'] = f[i + 2].split('|')[2]
                ingr.append(temp_dict)
                i += 1
            cook_dict[dish] = ingr
            i += 3
    return cook_dict

def get_shop_list_by_dishes(dishes, person_count, filename='recipes.txt'):
    result = {}
    for dish in dishes:
        ingredient_list = get_recipes(filename)[dish]
        for item in ingredient_list:
            ingredient_name = item['ingredient_name']
            ingredient_found = result.setdefault(ingredient_name,
                                                 {'measure': item['measure'],
                                                  'quantity': 5})
            ingredient_found['quantity'] = item['quantity'] * person_count
            result[ingredient_name] = ingredient_found
    return result
def for_cookbook():
    cook_book = get_recipes('recipes.txt')
    print('***** Книга рецептов *****')
    pp.pprint(cook_book)
    print('\n***** Необходимые покупки для блюд *****')
    pp.pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
if __name__ == "__main__":
    for_cookbook()