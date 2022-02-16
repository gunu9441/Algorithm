import sys

n = input()
n = n + ' '
length = len(n)
result = []
min_len = sys.maxsize
# 최대 자를 수 있는 길이: 전체 길이의 절반
for i in range(1, int(length//2)+1):
    # 초기화
    count = 1
    pre_char = n[:i]
    # i길이만큼 자르고 검사
    for j in range(i, length, i):
        #print('pre_char :', pre_char, ':', 'n[j:j+i] :', n[j:j+i])
        if ' ' == n[j:j+i]:
            if count == 1:
                result.append(pre_char)
                count = 1
            else:
                result.append(str(count)+pre_char)
                count = 1
        elif ' ' in n[j:j+i]:
            if count == 1:
                result.append(pre_char)
                n[j:j+i].replace(' ', '')
                result.append(n[j:j+i])
                count = 1
            else:
                result.append(str(count)+pre_char)
                n[j:j+i].replace(' ', '')
                result.append(n[j:j+i])
                count = 1
        else:
            if pre_char == n[j:j+i]:
                count += 1
            else:
                if count == 1:
                    result.append(pre_char)
                    pre_char = n[j:j+i]
                    count = 1
                else:
                    result.append(str(count)+pre_char)
                    pre_char = n[j:j+i]
                    count = 1
    result_string = "".join(result)
    # print(result_string)
    if min_len > len(result_string):
        answer = result_string
        min_len = len(result_string)
    result.clear()
# print(answer)
print(min_len)
