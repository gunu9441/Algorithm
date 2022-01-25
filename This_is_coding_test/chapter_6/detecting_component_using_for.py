import sys

input = sys.stdin.readline


def binary_detection(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None


#input = sys.stdin.readline
# given components
compo_n = int(input())
compo_list = list(map(int, input().split()))
compo_list.sort()
# print(compo_list)
# have to be detected components
detect_n = int(input())
detect_list = list(map(int, input().split()))
# print(detect_list)

for i in detect_list:
    #print('detect_comp: ', i)
    output = binary_detection(compo_list, i, 0, compo_n-1)
    if output != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
