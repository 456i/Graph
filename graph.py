GRAPH = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 6], [3, 7], [3, 8], [3, 9], [3, 10], [4, 11], [4, 12], [5, 13], [5, 14], [5, 15],
         [6, 17], [8, 18], [10, 19], [10, 20], [12, 21], [12, 22], [13, 23], [15, 24], [15, 25], [18, 26], [18, 27], [19, 28],
         [20, 29], [20, 30], [22, 31], [22, 31], [23, 33], [25, 34], [25, 35]]
COUNT_OF_APEX_new_tree = 15
APEXES_WITH_WEIGHTS = {apex: 1 for apex in range(1, 36)}
print(APEXES_WITH_WEIGHTS, 'this is apex with weights')
STACK = {}


def fill_STACK():
    global STACK
    for start_node, end_node in GRAPH:
        all_apexes = list(STACK.keys())
        if start_node in all_apexes:
            all_apex = STACK[start_node]
            all_apex.append(end_node)
        else:
            STACK[start_node] = {}
            STACK[start_node] = [end_node]


def descript_count_of_apexes_in_apex():
    global APEXES_WITH_WEIGHTS
    for apex in list(STACK.keys()):
        APEXES_WITH_WEIGHTS[apex] = len(list(STACK[apex]))


def dfs(start_apex, apex, count_of_containing_apexes, STACK):
    global finished_dict__, list_
    if apex in list(STACK.keys()):
        for node in STACK[apex]:
            list_.append(node)
            count_of_containing_apexes += APEXES_WITH_WEIGHTS[node]
            dfs(start_apex, node, count_of_containing_apexes, STACK)
    else:
        try:
            finished_dict__[start_apex] = count_of_containing_apexes
        except:
            finished_dict__ = {start_apex: count_of_containing_apexes}


def define_count_of_apex(dict):
    global finished_dict__, list_
    dict = dict.copy()
    dict.pop(1)
    list_ = []
    for apex, count_of_containing_apexes in dict.items():
        list_.append(apex)
        dfs(apex, apex, count_of_containing_apexes, STACK)

    print(finished_dict__, 'finished dict\n', list_, 'list')


fill_STACK()
descript_count_of_apexes_in_apex()
define_count_of_apex(APEXES_WITH_WEIGHTS)
print(APEXES_WITH_WEIGHTS, ' APEXES_WITH_WEIGHTS')
print(STACK)
