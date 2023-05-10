import networkx as nx
import matplotlib.pyplot as plt

# определение графа
graph =  [[1, 2], [1, 3], [2, 4], [2, 5]]

# создание графа
G = nx.Graph()

# добавление узлов
nodes = set(sum(graph, []))
for node in nodes:
    G.add_node(node)

# добавление ребер
for edge in graph:
    G.add_edge(edge[0], edge[1])

# отображение графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold')
plt.show()
