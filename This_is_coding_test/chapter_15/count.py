n, x = map(int, input().split())
num = list(map(int, input().split()))


def start_idx(num, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if num[mid] == target and (mid == 0 or num[mid-1] < num[mid]):
            return mid
        elif num[mid] > target or (num[mid] == target and num[mid] == num[mid-1]):
            end = mid - 1
        else:
            start = mid + 1
    return None


def end_idx(num, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if num[mid] == target and (mid == end or num[mid+1] > num[mid]):
            return mid
        elif num[mid] < target or (num[mid] == target and num[mid] == num[mid+1]):
            start = mid + 1
        else:
            end = mid - 1
    return None


st = start_idx(num, x, 0, len(num)-1)
ed = end_idx(num, x, 0, len(num)-1)

if st == None:
    print(-1)
else:
    print(ed - st + 1)
