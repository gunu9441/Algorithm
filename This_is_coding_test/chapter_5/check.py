import sys


def dfs(v):
    global visited, graph, count
    visited[v] = True
    count += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


input = sys.stdin.readline
count = -1
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    print(graph)
    print(visited)
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(1)
print(count)
