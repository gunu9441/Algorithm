import sys
# 최소 동전의 수 구하기
# Get the minimum number of coins

INT_MAX = sys.maxsize

n, m = map(int, input().split())
coins = list(map(int, input().split()))
dp = [
    INT_MAX for i in range(m+1)
]


def initialize():
    dp[0] = 0


initialize()

for i in range(1, m+1):
    for coin in coins:
        if coin <= i:
            if dp[i-coin] == INT_MAX:
                continue
            dp[i] = min(dp[i], dp[i-coin]+1)

answer = dp[m]
if answer == INT_MAX:
    answer = -1
print(answer)
