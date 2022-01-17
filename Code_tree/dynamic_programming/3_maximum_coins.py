# 최대 동전의 수 구하기
# Get the maximum number of coins

# My improved code
import sys

INT_MIN = -sys.maxsize

n, m = map(int, input().split())
coins = list(map(int, input().split()))
dp = [
    INT_MIN for _ in range(m+1)
]


def initialize():
    dp[0] = 0


initialize()
for i in range(1, m+1):
    for coin in coins:
        if i >= coin:
            if dp[i-coin] == INT_MIN:
                continue
            dp[i] = max(dp[i-coin]+1, dp[i])

answer = dp[m]
if answer == INT_MIN:
    answer = -1
print(answer)

# Solution

MIN_INT = -sys.maxsize

n, m = 3, 8
dp = [0]*(m+1)
coin = [0, 2, 3, 5]


def initialize():
    for i in range(m+1):
        dp[i] = INT_MIN
    dp[0] = 0


initialize()

for i in range(1, m+1):
    for j in range(1, n+1):
        if i >= coin[j]:
            if dp[i-coin[j]] == INT_MIN:
                continue
            dp[i] = max(dp[i], dp[i-coin[j]]+1)

ans = dp[m]
if ans == INT_MIN:
    ans = -1
print(ans)

# My origin code

INT_MIN = -sys.maxsize
MAX_NUM = 10000

n,  m = map(int, input().split())
coins = list(map(int, input().split()))
dp = [INT_MIN for _ in range(MAX_NUM+1)]


def initialize():
    dp[0] = 0
    for i in coins:
        dp[i] = 1


initialize()
for i in range(1, MAX_NUM+1):
    for j in range(1, i):
        for coin in coins:
            if j + coin == i:
                dp[i] = max(dp[i], dp[j]+1)

answer = dp[m]
if answer == INT_MIN:
    answer = -1
print(answer)

'''
# Remind

1. 최대 동전수를 구해야 하므로 dp 내부를 전부 -sys.maxsize로 초기화한다.
2. max_num으로 두지말고 input값으로 길이를 정한다.
3. dp[i-coin]을 통해 for문을 한번 더 안쓰고 풀 수 있다.
4. dp[0]를 0으로 초기화 하는 이유는 초기에 코인에 해당하는 dp 값은 -sys.maxsize인데
dp[i] = max(dp[i], dp[i-coin]+1)하게 되면 -sys.maxsize와 1을 비교하게 된다.
이에 1이 dp[i]에 등록되어 알맞은 flow로 진행될 수 있다.
'''
