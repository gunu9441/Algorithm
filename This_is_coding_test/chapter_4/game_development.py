map_size = list(map(int, input().split()))
*current_state, direction = list(map(int, input().split()))

total_map = list()
result = 1
check_exit_point = [0]*4
for i in range(map_size[1]):
    total_map.append(list(map(int, input().split())))
check_map = total_map.copy()
check_map[current_state[0]][current_state[1]] = 1

previous_state = current_state.copy()

while(1):
    direction = direction - 1
    if direction == -1:
        direction = 3
    if 0 not in check_exit_point:
        break

    if direction == 3:
        if check_map[current_state[0]][current_state[1]-1] == 1:
            check_exit_point[direction] = 1
            continue
        else:
            previous_state = current_state.copy()
            current_state[1] -= 1
            check_map[current_state[0]][current_state[1]] = 1
            result += 1

    elif direction == 2:
        if check_map[current_state[0]+1][current_state[1]] == 1:
            check_exit_point[direction] = 1
            continue
        else:
            previous_state = current_state.copy()
            current_state[0] += 1
            check_map[current_state[0]][current_state[1]] = 1
            result += 1

    elif direction == 1:
        if check_map[current_state[0]][current_state[1]+1] == 1:
            check_exit_point[direction] = 1
            continue
        else:
            previous_state = current_state.copy()
            current_state[1] += 1
            check_map[current_state[0]][current_state[1]] = 1
            result += 1
    elif direction == 0:
        if check_map[current_state[0]-1][current_state[1]] == 1:
            check_exit_point[direction] = 1
            continue
        else:
            previous_state = current_state.copy()
            current_state[0] -= 1
            check_map[current_state[0]][current_state[1]] = 1
            result += 1

print(result)

'''
*Reference
1. unpacking, packing: https://towardsdatascience.com/unpacking-operators-in-python-306ae44cd480
2. in, not in: https://pydole.tistory.com/entry/Python-%ED%8F%AC%ED%95%A8Containment-%EC%97%B0%EC%82%B0%EC%9E%90-in-not-in
3. list.copy(): https://inkkim.github.io/python/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EB%B3%B5%EC%82%AC/
4. id: https://wikidocs.net/20707,https://onsil-thegreenhouse.github.io/programming/python/2017/10/22/operator/
5. initialize 2D list: https://yechoi.tistory.com/52
6. and, or: https://wikidocs.net/22211
7. Python does not have pointer function: https://has3ong.tistory.com/136
'''
