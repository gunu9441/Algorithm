rows, columns = map(int, input().split())
graph = []
result = 0
for i in range(rows):
    graph.append(list(map(int, input())))

print(graph)


def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    if x <= -1 or x >= rows or y <= -1 or y >= columns:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    else:
        return False


for i in range(rows):
    for j in range(columns):
        if dfs(i, j) == True:
            result += 1
print(result)
