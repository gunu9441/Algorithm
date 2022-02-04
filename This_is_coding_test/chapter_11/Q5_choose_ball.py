a = []
n, m = map(int, input().split())
weight = list(map(int, input().split()))
count = 0
result = []


def recursive(start):
    global a, count, result
    print('r_start:', start)
    print(a)

    if len(a) >= 2:
        count += 1
        result.append(a)
        return

    for idx, i in enumerate(weight):
        #print(idx, i)
        if start > idx:
            continue
        if len(a) >= 1 and a[-1] == i:
            continue
        else:
            a.append(i)
            recursive(idx+1)
            # recursive(start+1) 이라고 하게되면 작동 X
            a.pop()


recursive(0)
# print(result)
print(count)
