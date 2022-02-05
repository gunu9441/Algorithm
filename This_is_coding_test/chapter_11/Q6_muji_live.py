food_time = list(map(int, input().split()))
k = int(input())


def resume_food():
    global food_time, k
    last_idx = -1
    idx = 0
    i = 0
    length = len(food_time)
    while True:
        if k == 0 or sum(food_time) == 0:
            break
        if food_time[idx] != 0:
            food_time[idx] -= 1
        else:
            k = k+1
        idx = (idx+1) % length
        last_idx = idx
        k -= 1
    # print(last_idx)
    # print(food_time)
    start = last_idx
    while True:
        if food_time[start] != 0:
            return start

        else:
            start += 1
            start = (start+1) % length

        if last_idx == start:
            return -1


answer = resume_food()
print(answer+1)
