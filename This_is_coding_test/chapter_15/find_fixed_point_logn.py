n = int(input())
num = list(map(int, input().split()))


def bisect(array, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == mid:
            return mid
        elif array[mid] < mid:
            start = mid + 1
        else:
            end = mid - 1
    return None


index = bisect(num, 0, len(num)-1)
if index == None:
    print(-1)
else:
    print(index)
