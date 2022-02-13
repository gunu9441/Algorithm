import sys

n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

home_list = [
    (i, j)
    for i in range(n)
    for j in range(n)
    if grid[i][j] == 1
]

store_list = [
    (i, j)
    for i in range(n)
    for j in range(n)
    if grid[i][j] == 2
]
#print('home_list:', home_list)
#print('store_list: ', store_list)
used_store_list = []
min_dist = sys.maxsize


def best_distance():
    global home_list, used_store_list
    result = 0
    for i in home_list:
        minimum = sys.maxsize
        for j in used_store_list:
            dist = abs(i[0]-j[0]) + abs(i[1]-j[1])
            if dist < minimum:
                minimum = dist
        result += minimum
    return result


def recursive(start):
    global min_dist
    if len(used_store_list) == m:
        # print(used_store_list)
        result = best_distance()
        if result < min_dist:
            min_dist = result
        return

    for i in range(start, len(store_list)):
        used_store_list.append(store_list[i])
        recursive(i+1)
        used_store_list.pop()


recursive(0)
print(min_dist)
