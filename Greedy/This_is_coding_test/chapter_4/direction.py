map_width = int(input())
map_size = (map_width, map_width)

raw_schedule = input().split()
current_state = [1, 1]
for i in raw_schedule:
    if i == 'L':
        if current_state[1] == 1:
            continue
        current_state[1] -= 1
    if i == 'R':
        if current_state[1] == map_size:
            continue
        current_state[1] += 1
    elif i == 'U':
        if current_state[0] == 1:
            continue
        current_state[0] -= 1
    elif i == 'D':
        if current_state[0] == map_size:
            continue
        current_state[0] += 1
    else:
        print("command error")

print(current_state)
'''
1. difference between '==' and 'is': https://ponyozzang.tistory.com/292
    list2 = [1, 2, 3]
    list2 = [1, 2, 3]
    list1 == list2
    >>> True
    
    list1 is list2 #list1 and list2 are not same objects that is stored in different memory addresses.
    >>> False
2. python None type
    python None is equal to null type in c++.

'''
