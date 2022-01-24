import sys
input = sys.stdin.readline
INT_MIN = -sys.maxsize

n, m = map(int, input().split())
s = [
    0 for _ in range(n+1)
]
e = [
    0 for _ in range(n+1)
]
v = [
    0 for _ in range(n+1)
]

for i in range(1, n+1):
    s[i], e[i], v[i] = map(int, input().split())
dp = [
    [INT_MIN for _ in range(n+1)]
    for _ in range(m+1)
]


def initialize():
    for i in range(1, n+1):
        if s[i] == 1:
            dp[1][i] = 0


initialize()

for i in range(2, m+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if s[k] <= i-1 and i - 1 <= e[k] and s[j] <= i and i <= e[j]:
                dp[i][j] = max(dp[i][j], dp[i-1][k] + abs(v[j]-v[k]))


print(max(dp[m]))
