n = int(input())
input_list = [list(input().split()) for _ in range(n)]

input_list.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in input_list:
    print(i[0])
