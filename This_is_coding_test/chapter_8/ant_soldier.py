num = int(input())
array = list(map(int, input().split()))
d = [0] * 100

d[0] = array[0]
d[1] = max(array[1], array[0])
for i in range(2, num):
    d[i] = max(d[i-2]+array[i], d[i-1])

print(d[num-1])
