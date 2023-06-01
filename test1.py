import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Apex:
    def __init__(self, graph):
        self.graph = graph
        self.G = nx.Graph()
        self.dict = STACK
        self.node_colors = {}
        self.list_of_nodes = list(self.dict.keys())
        self.pos = None
        self.fig = None
        self.ax = None
        self.visited_apexes = [1, 1]
        self.create_graph()

    def create_graph(self):
        nodes = set(sum(self.graph, []))
        self.G.add_nodes_from(nodes)
        self.G.add_edges_from(self.graph)

    def change_color(self, node, color):
        node_colors = {n: 'lightblue' for n in self.G.nodes}
        node_colors[node] = color
        return node_colors

    def get_lowest_apex(self, enter_node=None, old_node=None, count_of_apexes=0):
        self.nodes = enter_node
        self.old_node = old_node
        self.count_of_apexes = count_of_apexes
        self.nodes = list(self.dict.keys()) if enter_node is None else self.nodes
        for self.apex in self.nodes:
            self.visited_apexes.append(self.apex)
            if self.apex in self.list_of_nodes:
                self.old_node = self.apex
                if self.old_node < self.apex:
                    self.old_node = self.apex
                self.lowest_apex = self.dict[self.apex]
                self.count_of_apexes += 1
                self.get_lowest_apex(self.lowest_apex, self.old_node, self.count_of_apexes)
        return [2, 6, 17, 3, 7, 8, 18, 26, 27, 9, 10, 19, 28, 20, 29, 30, 4, 11, 12, 21, 22, 31, 31, 5, 13, 23, 33, 14, 15, 24, 25, 34, 35, 16, 6, 17, 7, 8, 18, 26, 27, 9, 10, 19, 28, 20, 29, 30, 11, 12, 21, 22, 31, 31, 13, 23, 33, 14, 15, 24, 25,
                34, 35, 16, 17, 18, 26, 27, 19, 28, 20, 29, 30, 21, 22, 31, 31, 23, 33, 24, 25, 34, 35, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

    def draw_graph(self, node, ax):
        ax.clear()
        node_colors = self.change_color(node, 'pink')
        nx.draw_kamada_kawai(self.G, node_color=list(node_colors.values()), with_labels=True)


class GraphAnimator:
    def __init__(self, graph):
        self.apex = Apex(graph)
        self.fig, self.ax = plt.subplots()
        self.get_LIST_WITH_APEXES = True
        self.is_animation_running = False
        self.i = -1

    def start_animation(self):
        self.apex.pos = nx.spring_layout(self.apex.G)

        def update_frame(framenum):
            self.i += 1

            if self.get_LIST_WITH_APEXES:
                self.node_to_update = self.apex.get_lowest_apex()
                self.get_LIST_WITH_APEXES = False

            if self.i >= len(self.node_to_update):
                self.i = 0

            self.apex.draw_graph(self.node_to_update[self.i], self.ax)

        self.animation = FuncAnimation(self.fig, update_frame, cache_frame_data=False, interval=1000, repeat=False)

        def on_key_press(event):
            if event.key == ' ':
                if self.is_animation_running:
                    self.animation.event_source.stop()
                    self.is_animation_running = False
                else:
                    self.animation.event_source.start()
                    self.is_animation_running = True

        self.fig.canvas.mpl_connect('key_press_event', on_key_press)
        plt.show()


# Пример использования
STACK = {
    1: [2, 3, 4, 5], 2: [6], 3: [7, 8, 9, 10], 4: [11, 12], 5: [13, 14, 15, 16], 6: [17], 8: [18], 10: [19, 20], 12: [21, 22], 13: [23], 15: [24, 25],
    18: [26, 27], 19: [28], 20: [29, 30], 22: [31, 31], 23: [33], 25: [34, 35]
}

graph = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [3, 10], [4, 11], [4, 12], [5, 13], [5, 14], [5, 15],
         [5, 16], [6, 17], [8, 18], [10, 19], [10, 20], [12, 21], [12, 22], [13, 23], [15, 24], [15, 25], [18, 26], [18, 27],
         [19, 28], [20, 29], [20, 30], [22, 31], [22, 31], [22, 32], [23, 33], [25, 34], [25, 35]]

animator = GraphAnimator(graph)
animator.start_animation()
