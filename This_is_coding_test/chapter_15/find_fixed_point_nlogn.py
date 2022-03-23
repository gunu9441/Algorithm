n = int(input())
num = list(map(int, input().split()))


def bisect(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None


count = 0
for i in range(len(num)):
    if i == bisect(num, i, 0, len(num)-1):
        count += 1
        print(i)

if count == 0:
    print(-1)
