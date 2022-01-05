existing_components_num = int(input())
existing_components = list(map(int, input().split()))
existing_components.sort()
order_num = int(input())
order_components = list(map(int, input().split()))

answer = []


def binary_search(array, start, end, target):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, start, mid-1, target)
    else:
        return binary_search(array, mid+1, end, target)


for target in order_components:
    result = binary_search(existing_components, 0,
                           existing_components_num-1, target)
    if result == None:
        answer.append('no')
    else:
        answer.append('yes')

print(answer)
