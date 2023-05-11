from pprint import pprint
def read_cook_book(file):
    data = {}
    key = ['ingredient_name', 'quantity', 'measure']
    with open(file, 'r', encoding='utf-8') as f:
        while True:
            ingredients = []
            name = f.readline().rstrip()
            if not name:
                break
            ingredient_count = f.readline().rstrip()
            for i in range(int(ingredient_count)):
                ing = f.readline().rstrip()
                ing_list = ing.strip().split("|")
                ingredient = dict(zip(key, ing_list))
                ingredient['quantity'] = int(ingredient['quantity'])
                ingredients.append(ingredient)
            data[name] = ingredients
            f.readline().rstrip()
    return data

file = 'recipes.txt'
data = read_cook_book(file)
pprint(data)