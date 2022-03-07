import sys

n = int(input())
place = list(map(int, input().split()))
# 최소 합을 구하기 위한 MIN
MIN = sys.maxsize

# 최소합일 때의 antena의 위치
antena = -1


# 안테나 설정
for i in range(1, max(place)+1):
    result = 0
    # 모든 집을 가져오기
    for j in place:
        result += abs(i-j)
    # 가장 작은 값을 antena로 설정
    if result == MIN and i < antena:
        antena = i
    if result < MIN:
        MIN = result
        antena = i


print(antena)
