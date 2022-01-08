for i in range(1, 20):
    for j in range(1, 20):
        if j % 2 == 0:
            print('{} * {} = {}'.format(i, j, i*j))
        elif j % 19 == 0:
            print('{} * {} = {}'.format(i, j, i*j))
        else:
            print('{} * {} = {} / '.format(i, j, i*j), end=' ')


num = int(input())
Arr = list(map(int, input().split()))
INF = int(1e11)


def count(array: list) -> tuple:
    min_value = INF
    cnt = 0
    for i in array:
        if i < min_value:
            min_value = i
            cnt = 1
        elif i == min_value:
            cnt += 1
        else:
            continue
    return (min_value, cnt)


answer = count(Arr)
print(answer[0], answer[1])

input_string, sequence = input().split()
sequence = int(sequence)
orders = []

for i in range(sequence):
    orders.append(int(input()))
length = len(input_string)


def first_operation(input_string: str):
    transformed_string = input_string[1:length]
    transformed_string += input_string[0]
    return transformed_string


def second_opeartion(input_string: str):
    transformed_string = input_string[length-1]
    transformed_string += input_string[0:length-1]
    return transformed_string


def third_opeartion(input_string: str):
    transformed_string = input_string[::-1]
    return transformed_string


for i in orders:
    if i == 1:
        input_string = first_operation(input_string)
        print(input_string)
    if i == 2:
        input_string = second_opeartion(input_string)
        print(input_string)
    if i == 3:
        input_string = third_opeartion(input_string)
        print(input_string)
