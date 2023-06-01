# Ссылка на задачу https://acmp.ru/index.asp?main=task&id_task=24
# Link to task https://acmp.ru/index.asp?main=task&id_task=24
list_of_trees = [tree for tree in range(1, 11)]
print(list_of_trees)
num__of_tree = int(input('Колличество оставшиехся деревьев '))
cases = 0
balance = 0
for k in range(len(list_of_trees)//num__of_tree):
    if k > 1:
        balance = k - 1
    if k == 0:
        k = 1
    cases += len(list_of_trees) - num__of_tree * k - balance + 1

    print(cases)

for i in range(cases):
    print(i+1, ' _ _ _ _ _ _ _ _ _ _')
