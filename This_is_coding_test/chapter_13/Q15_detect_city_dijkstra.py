import heapq
import sys

n, m, k, x = map(int, input().split())
INT_MAX = sys.maxsize
graph = [
    [] for _ in range(n+1)
]
distance = [INT_MAX for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

# print(graph)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(x)
print(distance)
count = 0
for idx, cost in enumerate(distance):
    if cost == k:
        count += 1
        print(idx)
if count == 0:
    print('-1')
