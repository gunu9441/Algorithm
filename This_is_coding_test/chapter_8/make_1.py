
# By using queue
from collections import deque

x = int(input())
count = 0


def bfs(x, count):
    queue = deque()
    queue.append((x, count))
    while queue:
        number, count = queue.popleft()
        if number == 1:
            break
        if number % 5 == 0:
            queue.append((number/5, count+1))
        if number % 3 == 0:
            queue.append((number/3, count+1))
        if number % 2 == 0:
            queue.append((number/2, count+1))
        queue.append((number-1, count+1))
    return count


print(bfs(26, 0))

# By using dynamic programming
x = int(input())
d = [0] * 30001

for i in range(2, x+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)
print(d[:26])
print(d[x])
