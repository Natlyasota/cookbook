import pprint
pp = pprint.PrettyPrinter(indent=2)
import os
file_path = os.path.join(os.getcwd(), 'recipes.txt')

def get_recipes(filename):
    result = {}
    with open(filename, encoding='utf-8') as recipes:
        line = recipes.readline()
        recipe_name = None
        ingredient_count = -1
        while line != '':
            line = line.strip()
            if recipe_name is None:
                recipe_name = line
                result[recipe_name] = []
                line = recipes.readline()
                continue
            if ingredient_count < 0:
                try:
                    ingredient_count = int(line)
                except ValueError as e:
                    return {}
            elif ingredient_count == 0:
                recipe_name = None
                ingredient_count = -1
            else:
                tmp_dict = dict(zip(
                    ['ingredient_name', 'quantity', 'measure'],
                    [x.strip() for x in line.split('|')]))
                try:
                    tmp_dict['quantity'] = int(tmp_dict.setdefault('quantity', 0))
                except ValueError as e:
                    return {}
                result[recipe_name].append(tmp_dict)
                ingredient_count -= 1
            line = recipes.readline()
    return result

def get_shop_list_by_dishes(dishes, person_count, filename='recipes.txt'):
    result = {}
    for dish in dishes:
        ingredient_list = get_recipes(filename)[dish]
        for item in ingredient_list:
            ingredient_name = item['ingredient_name']
            ingredient_found = result.setdefault(ingredient_name,
                                             {'measure': item['measure'],
                                             'quantity': 0})
            ingredient_found['quantity'] = ingredient_found['quantity'] + \
            item['quantity'] * person_count
            result[ingredient_name] = ingredient_found
    return result

def for_cookbook():
        print('***** Книга рецептов *****')
        cook_book = get_recipes('recipes.txt')
        pp.pprint(cook_book)
        print('\n***** Необходимые покупки для блюд *****')
        pp.pprint(get_shop_list_by_dishes(['Омлет', \
                                           'Утка по-пекински', 'Омлет', 'Омлет', 'Утка по-пекински'], 5))


if __name__ == "__main__":
  for_cookbook()