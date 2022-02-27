from itertools import combinations
import copy

n = int(input())
grid = [
    list(input().split())
    for _ in range(n)
]
temp = []
coordinates = []


def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n


def monitor_straight(x, y, dx, dy):
    print('x:', x)
    print('y:', y)
    new_x, new_y = x+dx, y+dy
    print('new_x:', new_x)
    print('new_y:', new_y)
    if not in_range(new_x, new_y) or temp[new_x][new_y] == 'O':
        return True
    else:
        if temp[new_x][new_y] == 'S':
            return False
        else:
            return monitor_straight(new_x, new_y, dx, dy)


def monitor(x, y):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    for dx, dy in zip(dxs, dys):
        print(dx, dy)
        if not monitor_straight(x, y, dx, dy):
            return False
    return True


success = 0

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'X':
            coordinates.append((i, j))

count = 0
teacher_count = 0
for obstacles in combinations(coordinates, 3):
    temp = copy.deepcopy(grid)
    for x, y in obstacles:
        temp[x][y] = 'O'
    for i in range(n):
        for j in range(n):
            if temp[i][j] == 'T':
                teacher_count += 1
                result = monitor(i, j)
                if result:
                    count += 1
    print(teacher_count, count)
    if teacher_count == count:
        success = 1
        break
    else:
        count = 0
        teacher_count = 0


if success:
    print('YES')
else:
    print('NO')

# 초기화 꼭 해줄 것 51행
# grid 쓰지 않고 temp로 해줘야하는데 grid 써서 틀렸음 조심!
