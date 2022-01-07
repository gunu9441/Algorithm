import heapq

INF = int(1e9)
city_num, path_num, start_city = map(int, input().split())
distance = [INF]*(city_num+1)
graph = [[] for _ in range(city_num+1)]
for i in range(path_num):
    x, y, cost = map(int, input().split())
    graph[x].append((y, cost))


def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (start, 0))
    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))


dijkstra(start_city)
valid_num = 0
max_time = 0

for i in range(1, city_num+1):
    if distance[i] != INF:
        valid_num += 1
        max_time = max(max_time, distance[i])

print(valid_num-1, end=' ')
print(max_time, end=' ')
