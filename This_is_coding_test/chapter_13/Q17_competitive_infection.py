import copy


n, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
s, x, y = map(int, input().split())

temp = copy.deepcopy(grid)


def can_go(x, y):
    if in_range(x, y) and temp[x][y] == 0:
        return True
    return False


def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n


def move(x, y, virus):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x+dx, y+dy
        if can_go(new_x, new_y):
            temp[new_x][new_y] = virus


for time in range(s):
    for virus in range(1, k+1):
        for i in range(n):
            for j in range(n):
                if grid[i][j] == virus:
                    move(i, j, virus)

print(temp[x-1][y-1])
