from collections import deque
# n: 보드 크기
# k: 사과 개수
n = int(input())
k = int(input())

# snake_list: 뱀 위치
# apple_list: apple 위치
snake_list = [
    [0 for _ in range(n+1)]
    for _ in range(n + 1)
]
snake = []
apple_list = [
    [0 for _ in range(n+1)]
    for _ in range(n+1)
]
order_list = []


def initialize():
    for i in range(k):
        x, y = map(int, input().split())
        apple_list[x][y] = 1

    snake_list[1][1] = 1
    n = int(input())
    for i in range(n):
        order_list.append(tuple(input().split()))


def in_range(x, y):
    return x >= 1 and x <= n and y >= 1 and y <= n


def cango(x, y):
    # 범위 안에 있고 뱀의 꼬리가 없을 경우 가능
    if in_range(x, y) and snake_list[x][y] == 0:
        return True
    return False


initialize()
# 우 하 좌 상
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
cur_dir = 0
x, y = 1, 1
time = 0
q = deque([(x, y)])
while True:
    print(q)
    for i in range(n):
        for j in range(n):
            print(snake_list[i][j], end=' ')
        print()
    time += 1
    new_x, new_y = x+dx[cur_dir], y+dy[cur_dir]
    if cango(new_x, new_y):
        snake_list[new_x][new_y] = 1
        q.append((new_x, new_y))
        if apple_list[new_x][new_y] == 1:
            apple_list[new_x][new_y] = 0
        else:
            x, y = q.popleft()
            snake_list[x][y] = 0
        x, y = new_x, new_y
    else:
        break
    for i in order_list:
        if time == int(i[0]):
            # 오른쪽으로 회전
            if i[1] == 'D':
                cur_dir = (cur_dir + 1) % 4
            # 왼쪽으로 회전
            else:
                cur_dir = (cur_dir - 1) % 4
print(time)
