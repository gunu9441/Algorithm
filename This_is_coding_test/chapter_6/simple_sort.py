num = int(input())
number_list = []
for i in range(num):
    number_list.append(int(input()))

number_list.sort(reverse=True)
for i in range(len(number_list)):
    print(number_list[i], end=' ')
