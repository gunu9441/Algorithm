# key = [
#    list(map(int, input().split()))
#    for _ in range(3)
# ]
# lock = [
#    list(map(int, input().split()))
#    for _ in range(3)
# ]
from sqlalchemy import false


key = [
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 1]
]
lock = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]


new_lock = []


def initialize():
    global lock, new_lock
    new_lock = [
        [0
         for _ in range(9)]
        for _ in range(9)
    ]
    for i in range(3):
        for j in range(3):
            new_lock[3+i][3+j] = lock[i][j]


def rotation(key):
    new_key = [
        [0
         for _ in range(3)]
        for _ in range(3)
    ]
    for i in range(3):
        for j in range(3):
            new_key[j][3-i-1] = key[i][j]
    return new_key


def check():
    for i in range(3, 6):
        for j in range(3, 6):
            if new_lock[i][j] != 1:
                return False
    return True


def solution():
    initialize()
    # 4번 rotation
    for _ in range(4):
        new_key = rotation(key)
        for i in range(6):
            for j in range(6):
                for k in range(3):
                    for g in range(3):
                        new_lock[i+k][j+g] += new_key[k][g]
                if check():
                    # print(new_lock)
                    return True
                for k in range(3):
                    for g in range(3):
                        new_lock[i+k][j+g] -= new_key[k][g]

        return False


if solution():
    print('true')
else:
    print('false')
