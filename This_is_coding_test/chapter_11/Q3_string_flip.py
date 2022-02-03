s = input()
stat = s[0]
num = 0
for i in range(1, len(s)):
    #print(stat, s[i])
    if stat != s[i]:
        num += 1
        stat = s[i]
    else:
        continue
# print(num)
result = num // 2 + num % 2
print(result)
