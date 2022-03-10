import heapq

n = int(input())
dp = [
    -1 for _ in range(n)
]
num = []
for _ in range(n):
    num.append(int(input()))
num.sort()

q = []
for i in range(0, n):
    heapq.heappush(q, num[i])
print('inital q:', q)
a = []
while q:
    print('q:', q)
    v1 = heapq.heappop(q)
    if len(q) == 0:
        result = v1
        break
    v2 = heapq.heappop(q)
    heapq.heappush(q, v1+v2)
    a.append(v1+v2)

print(a)
print(sum(a))
