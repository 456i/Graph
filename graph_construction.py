import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from graph import Apex, STACK
STACK = {1: [2, 3, 4, 5], 2: [6], 3: [7, 8, 9, 10], 4: [11, 12], 5: [13, 14, 15], 6: [17], 8: [18], 10: [19, 20], 12: [21, 22], 13: [23], 15: [24, 25], 18: [26, 27], 19: [28], 20: [29, 30], 22: [31, 31], 23: [33], 25: [34, 35]}
graph = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [3, 10], [4, 11], [4, 12], [5, 13], [5, 14], [5, 15],
         [6, 17], [8, 18], [10, 19], [10, 20], [12, 21], [12, 22], [13, 23], [15, 24], [15, 25], [18, 26], [18, 27], [19, 28],
         [20, 29], [20, 30], [22, 31], [22, 31], [23, 33], [25, 34], [25, 35]]
apex = Apex(STACK)


class GraphAnimator:
    def __init__(self, graph):
        self.G = nx.Graph()
        self.node_colors = {}
        self.pos = None
        self.fig = None
        self.ax = None
        self.animation = None
        self.is_running = True
        self.create_graph(graph)
        self.setup_plot()

    def create_graph(self, graph):
        nodes = set(sum(graph, []))
        for node in nodes:
            self.G.add_node(node)

        for edge in graph:
            self.G.add_edge(edge[0], edge[1])

    def setup_plot(self):
        self.pos = nx.spring_layout(self.G)
        self.fig, self.ax = plt.subplots()

    def change_color(self, node, color):
        node_colors = {n: 'blue' for n in self.G.nodes}

        node_colors[node] = color
        return node_colors

    def start_animation(self, apexes):
        def update_frame(framenum):
            color = 'red'
            node_ = apex.get_lowest_apex()
            node_colors = self.change_color(node_, color)
            self.ax.clear()
            nx.draw(self.G, self.pos, with_labels=True, node_color=list(node_colors.values()), ax=self.ax)

        self.animation = FuncAnimation(self.fig, update_frame, frames=12, interval=1000, repeat=False)

        def on_key_press(event):
            if event.key == ' ':
                if self.is_running:
                    self.animation.event_source.stop()
                    self.is_running = False
                else:
                    self.animation.event_source.start()
                    self.is_running = True

        self.fig.canvas.mpl_connect('key_press_event', on_key_press)
        plt.show()


animator = GraphAnimator(graph)
animator.start_animation([apex for apex in range(1, 36)])








