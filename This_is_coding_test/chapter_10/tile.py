import sys

n = int(input())
INT_MIN = - sys.maxsize
dp = [INT_MIN for _ in range(n+1)]


def initialize():
    dp[0] = 0
    dp[1] = 1
    dp[2] = 3


initialize()
for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2] * 2

print(dp)
print(dp[n])
