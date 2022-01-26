n, m = map(int, input().split())
command_list = []
parent = [i for i in range(n+1)]

for _ in range(m):
    command_list.append(tuple(map(int, input().split())))


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


for com_type, a, b in command_list:
    if com_type == 0:
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
    if com_type == 1:
        if find_parent(parent, a) != find_parent(parent, b):
            print('No')
        else:
            print('Yes')
