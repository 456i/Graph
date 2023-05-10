import random
import json

def write_to_json(tree):
    with open('test_1.json', 'a', encoding='utf-8') as json_file:
        json.dump(tree, json_file, indent=4)

def create_tree(tree, count):
    for i in range(count):
        # выбираем случайный ключ в дереве
        parent = random.choice(list(tree.keys()))
        # создаем новый узел
        node = {random.randint(10, 44): {}}
        # добавляем новый узел в дерево
        tree[parent].update(node)
    return tree

def make_feature_for_tree(page, dict):
    keys = list(dict[page].keys())
    for key in keys:
        for i in range(random.randint(4, 9)):
            try:
                dict[page][key][i] = {}
            except KeyError:
                dict[page][key] = {}
                dict[page][key][i] = {}
            try:
                dict[page][key][i] = random.randint(10, 30)
            except KeyError:
                pass
    print(dict)

# создаем дерево из одного корня
tree = {0: {}}

for i in range(7):
    new_tree = create_tree(tree, 150)
    make_feature_for_tree(0, new_tree)
    print('new tree:', new_tree)

write_to_json(new_tree)