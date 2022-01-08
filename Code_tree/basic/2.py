n, m = map(int, input().split())
grid = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for i in range(m):
    for j in range(n):
        if i % 2 == 0:
            grid[j][i] = n*(i) + j
        if i % 2 == 1:
            grid[j][i] = n*(i+1) - j - 1

for i in grid:
    print(*i)
