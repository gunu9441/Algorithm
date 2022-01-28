import sys

INT_MAX = sys.maxsize

n, m = map(int, input().split())
coins = [0 for _ in range(n)]
dp = [INT_MAX for _ in range(m+1)]
for i in range(n):
    coins[i] = int(input())
# print(coins)


def initialize():
    dp[0] = 0


initialize()
for i in range(1, m+1):
    for coin in coins:
        if i >= coin:
            if dp[i-coin] == INT_MAX:
                continue
            dp[i] = min(dp[i], dp[i-coin] + 1)

if dp[m] == INT_MAX:
    print('-1')
else:
    print(dp[m])
