# My answer
# score = "".join(map(str, input())) -> input()만 사용해도 문자열로 찍혀서 이와 같이 해줄 필요 X
score = input()
length = len(score)

right = score[:int(length/2)]
left = score[int(length/2):]
print(right)
print(left)
if sum(map(int, list(right))) == sum(map(int, list(left))):
    print("LUCKY")
else:
    print("READY")
'''
1. slice할 때, length/2 라고 하면 float형이 되어 slice가 진행되지 않음.
이에 int를 붙혀 slicing하고 right와 left가 str형태로 들어가 있기 때문에 int로 형변환해서 sum 진행.
2. list()를 사용하므로써 문자열을 list로 분할 가능.
'''
# Solution
n = input()
length = len(n)
summary = 0

for i in range(length//2):
    summary += int(n[i])

for i in range(length//2, length):
    summary -= int(n[i])

if summary == 0:
    print("LUCKY")
else:
    print("READY")
'''
그냥 index로 접근해서 더하고 뺌으로써 결과 값이 0이나오면 LUCKY 출력. 아니라면 READY 출력
'''
