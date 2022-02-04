n = int(input())
coins = list(map(int, input().split()))
coins.sort()
length = len(coins)

# 나올 수 있는 돈의 모든 sum
result = []

# 사용할 돈 종류
money = []


def recursive(start, i):
    if len(money) == i: 
        result.append(sum(money))
        return
    for j in range(start, length):
        money.append(coins[j])
        recursive(j+1, i)
        money.pop()


for i in range(1, n+1):
    recursive(0, i)
# print(result)
result = list(set(result))
# print(result)
for i in range(1, sum(coins)+2):
    if i not in result:
        print(i)
        break
    
