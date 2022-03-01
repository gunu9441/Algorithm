from collections import deque
import copy

n, l, r = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


def can_go(x, y, visited):
    if in_range(x, y) and visited[x][y] == -1:
        return True
    return False


def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n


def bfs(x, y, index, visited):
    # 결속되어있는 index
    united = []
    united.append((x, y))
    # bfs 사용
    q = deque([(x, y)])
    visited[x][y] = index

    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        cur_x, cur_y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = cur_x + dx, cur_y + dy
            if can_go(new_x, new_y, visited):
                diff = abs(grid[new_x][new_y]-grid[cur_x][cur_y])
                if l <= diff and diff <= r:
                    q.append((new_x, new_y))
                    visited[new_x][new_y] = index
                    united.append((new_x, new_y))
    result = 0
    #print('united:', united)
    # print(len(united))
    for x, y in united:
        result += grid[x][y]
    #print('sum:', result)
    result //= len(united)
    #print('average:,', result)

    for x, y in united:
        grid[x][y] = result
    #print('grid:', grid)
    #print('visited:', visited)


total_count = 0
while True:
    # 1개의 step을 걸칠 때 마다 visited 초기화
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                bfs(i, j, index, visited)
                index += 1
    if index == n*n:
        break
    total_count += 1

print(total_count)
