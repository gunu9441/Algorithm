n, m = map(int, input().split())
parent = [0 for i in range(n+1)]
edges = []
answer = 0
sub_max = 0
value_list = []

for i in range(1, n+1):
    parent[i] = i


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


for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += cost
        #print('sub_max: ', sub_max, 'cost: ', cost)
        sub_max = max(sub_max, cost)
        #print('sub_max: ', sub_max, 'cost: ', cost)
        value_list.append(cost)


answer = answer - sub_max
# print(value_list)
print(answer)
