import heapq

INF = int(1e9)
company_num, path_num = map(int, input().split())
graph = [[] for i in range(company_num+1)]
distance_meeting = [INF]*(company_num+1)
distance_store = [INF]*(company_num+1)

for i in range(1, path_num + 1):
    start_node, end_node = map(int, input().split())
    graph[start_node].append((end_node, 1))
    graph[end_node].append((start_node, 1))

X, K = map(int, input().split())


def dijkstra(start, array):
    array[start] = 0
    q = []
    heapq.heappush(q, (start, 0))
    while q:
        now, dist = heapq.heappop(q)
        if array[now] < dist:
            continue

        for i in graph[now]:
            cost = dist+i[1]

        if cost < array[i[0]]:
            array[i[0]] = cost
            heapq.heappush(q, (i[0], cost))


dijkstra(1, distance_meeting)
dijkstra(K, distance_store)
if distance_meeting[K] == INF or distance_store[X] == INF:
    print('-1')
else:
    distance = distance_meeting[K] + distance_store[X]
    print(distance)
