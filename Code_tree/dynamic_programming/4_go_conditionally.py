# 조건에 맞게 선택적으로 전진하기
# go in the particualr coditions

# My code
import sys

INT_MIN = -sys.maxsize

n = int(input())
a = list(map(int, input().split()))
dp = [INT_MIN for i in range(n)]


def initialize():
    dp[0] = 0


initialize()

for i in range(1, n):
    for j in range(i):
        if a[j] >= i-j:
            dp[i] = max(dp[j]+1, dp[i])

answer = dp[n-1]
if answer == INT_MIN:
    answer = -1
print(answer)


# Solution
INT_MIN = -sys.maxsize

n = int(input())
a = list(map(int, input().split()))
dp = [INT_MIN for i in range(n)]


def initialize():
    dp[0] = 0


initialize()

for i in range(1, n):
    for j in range(i):
        if a[j] >= i-j:
            if dp[j] == INT_MIN:
                continue
            dp[i] = max(dp[j]+1, dp[i])

answer = dp[n-1]
if answer == INT_MIN:
    answer = -1
print(answer)
