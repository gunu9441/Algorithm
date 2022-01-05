n, search_num = map(int, input().split())
array = list(map(int, input().split()))
array.sort()


def binary_search(array, start, end, target):
    if start > end:
        return False
    mid = (start + end)//2

    if array[mid] == target:
        return mid
    if array[mid] > target:
        return binary_search(array, start, mid-1, target)
    if array[mid] < target:
        return binary_search(array, mid+1, end, target)


result = binary_search(array, 0, n-1, search_num)
if not result:
    print("{} does not exist.".format(search_num))
else:
    print("{} exists.".format(search_num))
