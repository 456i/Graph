import json
#
# graph = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [4, 9], [5, 10], [5, 11], [6, 12],
#          [6, 13], [7, 14], [7, 15], [8, 16], [8, 17], [9, 18], [9, 19], [9, 20], [10, 21], [11, 22], [11, 23],
#          [12, 24], [12, 25], [13, 26], [13, 27], [13, 28]]
#
#
# def make_graph(edges: list, assortment: dict, start_node: int):
#     for node in edges:
#         start_el = node[0]
#         if start_el == start_node:
#             end = node[1]
#             path = dfs({i: [node[1] for node in graph if node[0] == i] for i in range(1, 29)}, 1, end)
#             unpack_dict_and_write(assortment, path)
#     print(assortment)
#     return assortment
#
#
# def unpack_dict_and_write(dict__, path):
#     dict_ = dict__
#     for i in path[:-1]:
#         if i not in dict_:
#             dict_[i] = {}
#         dict_ = dict_[i]
#     dict_[path[-1]] = {}
#
#
# def write_to_json():
#     with open('test.json', 'w', encoding='utf-8') as json_file:
#         json.dump(dict, json_file, indent=3)
#
#
# def dfs(graph, start, end, path=[]):
#     path = path + [start]
#     print(path)
#     if start == end:
#         return path
#     for node in graph[start]:
#         if node not in path:
#             newpath = dfs(graph, node, end, path)
#             if newpath:
#                 return newpath
#     return None


def upload_data():
    global dict
    with open('test.json', 'r') as json_file:
        dict = json.load(json_file)


def make_mass_list(dict):
    keys = list(dict.keys())
    dict__ = dict.copy()
    for key in keys:
        newdict = dict__[key]
        newdict__ = newdict.copy()
        print(newdict__)
        make_mass_list(newdict__)



upload_data()
make_mass_list(dict)























#
#
#
# if __name__ == '__main__':
#     dict = {[1, 0]: {}}
#     for n in range(1, 28):
#         make_graph(graph, dict, n)
#
#     write_to_json()
