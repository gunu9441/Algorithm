n = int(input())
ele_list = list(map(int, input().split()))
ele_list.sort()
count = 0
result = 0

for i in ele_list:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)
