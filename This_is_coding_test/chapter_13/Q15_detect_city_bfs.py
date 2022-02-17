import sys
from collections import deque

INT_MAX = sys.maxsize

input = sys.stdin.readline
n, m, k, x = map(int, input().split())
distance = [INT_MAX for _ in range(n+1)]
graph = [
    [] for i in range(n+1)
]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
visited = [False for _ in range(n+1)]

distance[x] = 0


def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                distance[i] = distance[v] + 1
                q.append(i)
                visited[i] = True


bfs(x)
count = 0
print(distance)
for idx, i in enumerate(distance):
    if i == k:
        count += 1
        print(idx)

if count == 0:
    print(-1)
