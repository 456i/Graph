import random


def dfs__(graph, start):
    stack = [start]
    visited = []  # Используем set вместо списка для посещенных вершин
    while stack:
        vertex = stack.pop()
        visited.append(vertex)
        neighbors = [node[1] for node in graph if node[0] == vertex]  # Получаем только второй элемент ребра
        stack.extend([n for n in neighbors if n not in visited])
    return visited


def find_min_of_destroyed_roads(m_o_d_r, list):
    list_with_weight = []
    # for n in list:
    #     print(n[1])
    #     if n[1] == m_o_d_r:
    #         list_with_weight.append(n[1])
    list_with_weight.append(n[1] for n in list if n[1] == m_o_d_r)
    if list_with_weight:
        print(f'была найдена ветка, содержащая указанное количество деревень\nМинимальное количество сломанных дорог -> 1')
    else:
        list_with_approximately_weght = []
        list_with_approximately_weght = [[apex, weight] for apex, weight  in list_with_weight]
        print(list_with_approximately_weght)

graph = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [3, 10], [4, 11], [4, 12], [5, 13], [5, 14], [5, 15],
         [5, 16], [6, 17], [8, 18], [10, 19], [10, 20], [12, 21], [12, 22], [13, 23], [15, 24], [15, 25], [18, 26], [18, 27],
         [19, 28], [20, 29], [20, 30], [22, 31], [22, 31], [22, 32], [23, 33], [25, 34], [25, 35]]

apex_with_weight = []
for apex in range(1, 36):
    result = dfs__(graph, apex)
    apex_with_weight.append([apex, len(result)])


print(random.randint(1,25))
print(apex_with_weight)
left_villages = int(input('Введите количество оставшихся деревень '))
find_min_of_destroyed_roads(left_villages, apex_with_weight)
