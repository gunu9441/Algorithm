

def practice(i):
    print('practice_{} 호출'.format(i))
    if i == 0:
        print('practice_0 return 직후 {}반환'.format(i))
        return i
    i = i-1
    print('practice_{} return 대기중'.format(i+1))
    return practice(i)+1


z = practice(3)
print(z)
