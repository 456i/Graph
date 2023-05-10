GRAPH = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [4, 8], [4, 9], [5, 10], [5, 11], [6, 12],
         [6, 13], [7, 14], [7, 15], [8, 16], [8, 17], [9, 18], [9, 19], [9, 20], [10, 21], [11, 22], [11, 23], [12, 24], [12, 25], [13, 26], [13, 27], [13, 28]]
COUNT_OF_APEX_new_tree = 5
APEXES_WITH_WEIGHTS = {apex: None for apex in range(1, 29)}
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


# class Apex:
#     def __init__(self, dictionary):
#         self.dict = dictionary
#         # self.trial_dict = self.dict.copy()
#         self.nodes = None
#         self.lowest_apex = None
#         self.enter_node = None
#         self.count_of_apexes = 0
#         self.old_node = None
#
#     def get_lowest_apex(self, enter_node=None, count_of_apexes=0, old_node=None):
#         self.nodes = enter_node
#         self.count_of_apexes = count_of_apexes
#         self.old_node = old_node
#         if enter_node is None:
#             self.nodes = list(self.dict.keys())
#         for self.apex in self.nodes:
#             try:
#                 self.lowest_apex = self.dict[self.apex]
#                 # del self.trial_dict[self.apex]
#                 print(self.lowest_apex)
#
#                 # sefl.count_of_apexes_for_tree_apex += 1
#                 APEXES_WITH_WEIGHTS[self.apex] = self.count_of_apexes
#                 self.count_of_apexes += 1
#                 self.get_lowest_apex(self.lowest_apex, self.count_of_apexes, self.old_node)
#                 # self.count_of_apexes_for_tree_apex = 0
#             except Exception as ex:
#                 # print('Exception -> ',ex)
#                 # APEXES_WITH_WEIGHTS[self.lowest_apex[0]] = self.count_of_apexes
#                 print(self.count_of_apexes)
#
#         self.count_of_apexes = 0


for apex in GRAPH:
    Node(apex[0], apex[1])









print(STACK)
make_node()
# apex = Apex(STACK)
# apex.get_lowest_apex()

print(STACK)


