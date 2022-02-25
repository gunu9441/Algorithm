import sys

MIN = sys.maxsize
MAX = -sys.maxsize

n = int(input())
number_list = list(map(int, input().split()))
operators = list(map(int, input().split()))

operators_order = []


def recursive():
    global MIN, MAX

    if len(operators_order) == n-1:
        result = number_list[0]
        for i in range(0, len(operators_order)):
            if operators_order[i] == 0:
                result += number_list[i+1]
            elif operators_order[i] == 1:
                result -= number_list[i+1]
            elif operators_order[i] == 2:
                result *= number_list[i+1]
            else:
                if result < 0:
                    result = -(-result // number_list[i+1])
                else:
                    result //= number_list[i+1]
        MIN = min(MIN, result)
        MAX = max(MAX, result)
    for i in range(4):
        if operators[i] == 0:
            continue
        operators[i] -= 1
        operators_order.append(i)
        recursive()
        operators_order.pop()
        operators[i] += 1


recursive()
print(MAX)
print(MIN)
