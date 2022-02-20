import copy
import sys
from itertools import combinations

n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
candidates = []
temp = []


def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < m


def can_go(x, y):
    if in_range(x, y) and temp[x][y] == 0:
        return True
    return False


def virus(x, y):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        if can_go(new_x, new_y):
            temp[new_x][new_y] = 2
            virus(new_x, new_y)


def safe_area_count():
    count = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                count += 1
    return count


def find_virus():
    virus = []
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                virus.append((i, j))
    return virus


for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            candidates.append((i, j))

max_area = - sys.maxsize
for a, b, c in combinations(candidates, 3):
    temp = copy.deepcopy(grid)
    temp[a[0]][a[1]] = 1
    temp[b[0]][b[1]] = 1
    temp[c[0]][c[1]] = 1

    init_virus = find_virus()
    for x, y in init_virus:
        virus(x, y)

    result = safe_area_count()
    if result > max_area:
        max_area = result

print(max_area)
