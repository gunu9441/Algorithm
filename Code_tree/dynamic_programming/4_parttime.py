import sys
input = sys.stdin.readline
INT_MIN = -sys.maxsize

n = int(input())
s = [
    0 for _ in range(n+1)
]
e = [
    0 for _ in range(n+1)
]
p = [
    0 for _ in range(n+1)
]
dp = [INT_MIN for _ in range(n+1)]

for i in range(1, n+1):
    s[i], e[i], p[i] = map(int, input().split())


def initialize():
    dp[0] = 0


initialize()

for i in range(1, n+1):
    for j in range(0, i):
        if e[j] < s[i]:
            dp[i] = max(dp[j]+p[i], dp[i])

print(max(dp))
