import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

graph = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [4, 9], [5, 10], [6, 11], [6, 12]]

G = nx.Graph()

nodes = set(sum(graph, []))
for node in nodes:
    G.add_node(node)

for edge in graph:
    G.add_edge(edge[0], edge[1])

pos = nx.spring_layout(G)


def change_color(_node, color):
    node_colors = {n: 'blue' for n in G.nodes}
    node_colors[_node] = color
    return node_colors


def update_frame(i):
    node_ = i + 1
    color = 'red'
    node_colors = change_color(node_, color)
    ax.clear()
    nx.draw(G, pos, with_labels=True, node_color=list(node_colors.values()), ax=ax)


fig, ax = plt.subplots()
animation = FuncAnimation(fig, update_frame, frames=12, interval=1000, repeat=False)


is_running = True


def on_key_press(event):
    global is_running
    if event.key == ' ':
        if is_running:
            animation.event_source.stop()
            is_running = False
        else:
            animation.event_source.start()
            is_running = True

fig.canvas.mpl_connect('key_press_event', on_key_press)

plt.show()
