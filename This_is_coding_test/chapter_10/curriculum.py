import sys
import copy
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [
    [] for _ in range(n+1)
]
time = [0 for i in range(n+1)]
indegrees = [0 for i in range(n+1)]

# list 초기화
for i in range(1, n+1):
    command = list(map(int, input().split()))
    length = len(command)
    for j in range(length):
        if command[j] == -1:
            break
        if j == 0:
            time[i] = command[j]
        else:
            graph[command[j]].append(i)
            indegrees[i] += 1
result = copy.deepcopy(time)
# print(time)
# print(indegrees)

# queue 초기화
q = deque()
for idx, indegree in enumerate(indegrees, start=1):
    if indegree == 0:
        q.append(idx)

# topology sort
while q:
    now = q.popleft()
    for i in graph[now]:
        indegrees[i] -= 1
        result[i] = max(result[i], result[now]+time[i])
        if indegrees[i] == 0:
            q.append(i)

for i in range(1, len(result)):
    print(result[i])
