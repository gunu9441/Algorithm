import sys

INT_MIN = -sys.maxsize
grid_size = []
grid_element = []
num_test = int(input())
answer = []


def initialize(dp, grid):
    for i in range(n):
        dp[i][0] = grid[i][0]


for i in range(num_test):
    grid_size.append(tuple(map(int, input().split())))
    grid_element.append(list(map(int, input().split())))

for i in range(num_test):
    n, m = grid_size[i]
    dp = [[INT_MIN
           for _ in range(m)]
          for _ in range(n)]
    grid = grid_element[i]
    curr_grid = [
        [0 for _ in range(m)]
        for _ in range(n)]

    for j in range(n):
        for k in range(m):
            curr_grid[j][k] = grid[(m)*j + k]
    initialize(dp, curr_grid)
    for k in range(1, m):
        for j in range(n):
            if j-1 >= 0:
                dp[j][k] = max(dp[j][k], dp[j-1][k-1]) + curr_grid[j][k]
            dp[j][k] = max(dp[j][k], dp[j][k-1] + curr_grid[j][k])
            if j+1 <= n-1:
                dp[j][k] = max(dp[j][k], dp[j+1][k-1] + curr_grid[j][k])
    # print(dp)
    answer.append(max([i[-1] for i in dp]))
for i in answer:
    print(i)
