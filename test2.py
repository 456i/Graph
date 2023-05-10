GRAPH = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [3, 10], [4, 11], [4, 12], [5, 13], [5, 14], [5, 15],
         [6, 17], [8, 18], [10, 19], [10, 20], [12, 21], [12, 22], [13, 23], [15, 24], [15, 25], [18, 26], [18, 27], [19, 28],
         [20, 29], [20, 30], [22, 31], [22, 31], [23, 33], [25, 34], [25, 35], ]
COUNT_OF_APEX_new_tree = 15
COUNT_NODES = len(GRAPH)-1
APEXES_WITH_WEIGHTS = {apex: None for apex in range(1, COUNT_NODES)}
print(APEXES_WITH_WEIGHTS, 'this is apex with weights')
STACK = {}


class Node:
    def __init__(self, start_node, end_node):
        self.start_node = start_node
        self.end_node = end_node
        self.all_apexes = list(STACK.keys())
        if self.start_node in self.all_apexes:
            all_apex = STACK[self.start_node]
            all_apex.append(self.end_node)
        else:
            STACK[self.start_node] = {}
            STACK[self.start_node] = [self.end_node]


def make_node():
    global STACK, APEXES_WITH_WEIGHTS
    STACK = {apex: len(apex_adjacent) for apex, apex_adjacent in STACK.items()}
    all_apexes = list(STACK.keys())
    all_apexes__ = list(APEXES_WITH_WEIGHTS.keys())
    print(all_apexes__, all_apexes)
    for apex in all_apexes:
        if apex in all_apexes__:
            all_apexes__.remove(apex)

    for apex in all_apexes__:
        STACK[apex] = 1


class Apex:
    def __init__(self, dictionary):
        self.dict = dictionary
        self.nodes = None
        self.lowest_apex = None
        self.enter_node = None
        self.count_of_apexes = 0
        self.old_node = None

    def get_lowest_apex(self, enter_node=None, old_node=None):
        self.nodes = enter_node
        self.old_node = old_node
        if enter_node is None:
            self.nodes = list(self.dict.keys())
        for self.apex in self.nodes:
            try:
                self.lowest_apex = self.dict[self.apex]
                self.get_lowest_apex(self.lowest_apex, self.old_node)

            except Exception as ex:
                print('Exception -> ', ex)

            print(self.lowest_apex)


for apex in GRAPH:
    Node(apex[0], apex[1])

print(STACK)
apex = Apex(STACK)
apex.get_lowest_apex()

print(STACK)
