# 직각 삼각형 안에서의 최대 합 구하기
# Get the maximum sum in right-alngled triangle

# My code
import sys
n = int(input())
a = [
    list(map(int, input().split()))
    for i in range(n)
]
dp = [
    [0 for i in range(n)]
    for i in range(n)
]


def initialization():
    dp[0][0] = a[0][0]
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + a[i][0]
        dp[i][i] = dp[i-1][i-1] + a[i][i]


initialization()

for i in range(2, n):
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + a[i][j]
print(max(dp[-1]))


# Solution
INT_MIN = -sys.maxsize
n = int(input())
a = [
    list(map(int, input().split()))
    for _ in range(n)
]
dp = [
    [0 for _ in range(n)]
    for _ in range(n)
]


def initialize():
    dp[0][0] = a[0][0]

    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + a[i][0]

    for i in range(1, n):
        dp[i][i] = dp[i-1][i-1] + a[i][i]


initialize()

for i in range(2, n):
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j],
                       dp[i-1][j-1]) + a[i][j]
ans = INT_MIN
for j in range(n):
    ans = max(ans, dp[n-1][j])
print(ans)

'''
# Remind
1. sys.maxsize 사용하기
import sys
    INT_MIN = -sys.maxsize


2. i 대신 _ 사용하기
dp = [
    [0 for _ in range(n)]
    for _ in range(n)
]


3. 2중 for문으로 직각 삼각형 구현할  때 주의하기
for  i in range(2,n):
    for j in range(1, i):
        ...

4. print(max(dp[-1]))
2차원 list의 dp에서 dp[-1]을 통해 마지막 행 가져온 이후,
max를 사용해 최대값 구하기
'''
