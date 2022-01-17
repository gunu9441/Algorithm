# 직각 사각형 안에서의 최대 합 구하기
# Get the maximum sum in rectangle

# My code
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
        dp[0][i] = dp[0][i-1] + a[0][i]


initialize()

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i][j-1],
                       dp[i-1][j])+a[i][j]
print(dp[n-1][n-1])


# Solution
n = int(input())

num = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [
    [0 for _ in range(n)]
    for _ in range(n)
]


def initialize():
    # 시작점의 경우 dp[0][0] = num[0][0]으로 초기값을 설정해줍니다
    dp[0][0] = num[0][0]

    # 최좌측 열의 초기값을 설정해줍니다.
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + num[i][0]

    # 최상단 행의 초기값을 설정해줍니다.
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + num[0][j]


# 초기값 설정
initialize()

# 탐색하는 위치의 위에 값과 좌측 값 중에 큰 값에
# 해당 위치의 숫자를 더해줍니다.
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + num[i][j]

print(dp[n-1][n-1])
