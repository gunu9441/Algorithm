# Detecting increased part in list
# 증가 부분 수열 뽑아내기


import sys

INT_MIN = -sys.maxsize
n = int(input())
dp = [INT_MIN for _ in range(n+1)]
a = [0 for _ in range(n+1)]
given_seq = list(map(int, input().split()))


def initialize():
    global given_seq, a, dp
    a[1:] = given_seq[:]
    dp[0] = 0
    a[0] = 0


initialize()
for i in range(1, n+1):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
