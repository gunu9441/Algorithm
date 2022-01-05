hour = int(input())

count = 0
# brute force method
for i in range(hour+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                # print(str(i)+str(j)+str(k))
                count += 1

print(count)

'''
1. '+' can concatenate strings.
2. 'in' : check the element if it exist in string.'
'''
