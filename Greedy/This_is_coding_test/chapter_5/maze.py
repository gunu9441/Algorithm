from collections import deque

rows, columns = map(int, input().split())
graph = []
for i in range(rows):
    graph.append(list(map(int, input())))
print(graph)
start = (0, 0)


def bfs(x, y):
    print('--3--')
    print(x)
    print(y)
    print('--3--')
    queue = deque()
    queue.append((x, y))
    while queue:
        v = queue.popleft()
        print(v)
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(len(dx)):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]
            if nx <= -1 or nx >= rows or ny <= -1 or ny >= columns:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[v[0]][v[1]] + 1
                queue.append((nx, ny))
            if nx == rows-1 and ny == columns-1:
                return graph[nx][ny]


print(bfs(*start))
