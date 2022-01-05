n, m = map(int, input().split())
length_list = list(map(int, input().split()))
length_list.sort()


def binary_search(array, start, end, target):
    answer = 0
    while start <= end:
        mid = (start+end)//2
        result = sum(map(lambda value: value - mid if value -
                         mid > 0 else 0, length_list))
        if result > target:
            answer = mid
            start = mid+1
        elif result < target:
            end = mid-1
        else:
            answer = mid
            return answer
    return answer


print(binary_search(length_list, 0, max(length_list), m))
