def dfs__(graph, start):
    stack = [start]
    visited = set()  # Используем set вместо списка для посещенных вершин

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            neighbors = [v[1] for v in graph if v[0] == vertex]  # Получаем только второй элемент ребра
            stack.extend([n for n in neighbors if n not in visited])
    return visited


graph = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [3, 10], [4, 11], [4, 12], [5, 13], [5, 14], [5, 15],
         [5, 16], [6, 17], [8, 18], [10, 19], [10, 20], [12, 21], [12, 22], [13, 23], [15, 24], [15, 25], [18, 26], [18, 27],
         [19, 28], [20, 29], [20, 30], [22, 31], [22, 31], [22, 32], [23, 33], [25, 34], [25, 35]]

for apex in range(1, 36):
    result = dfs__(graph, apex)
    print(apex, ' includes ', len(result), result)
