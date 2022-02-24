input_string = input()


def check(num):
    if num < 0:
        return False
    else:
        return True


def flip_brk(s):
    new_s = ''
    for i in s:
        if i == '(':
            new_s += ')'
        else:
            new_s += '('
    return new_s


def recursive(s):
    u = ''
    v = ''
    st_brk = 0
    ed_brk = 0
    # u v 나누기
    for i in s:
        if st_brk == ed_brk and st_brk != 0:
            v = v + i
        else:
            if i == '(':
                st_brk += 1
            else:
                ed_brk += 1
            u = u + i
    print('u:', u)
    print('v:', v)
    num = 0
    for i in u:
        if i == '(':
            num += 1
        else:
            num -= 1
            # ')'가 먼저 나온 경우가 weird하므로 이때만 check
            output = check(num)
            print('output:', output)
            if output:
                continue
            else:
                print('not correct u:', u)
                print('corresponding v:', v)
                new_string = '('
                new_string += recursive(v)
                new_string += ')'
                print('new_string:', new_string)
                # 첫번쨰와 마지막 문자열 삭제
                u = u[1:-1]
                print('modified_delete_first_end u:', u)
                # 괄호방향 뒤집기
                u = flip_brk(u)
                print('fliped_u:', u)
                # 붙히기
                new_string += u
                print('final_new_String:', new_string)
                return new_string
    # 종료 조건
    if v == '':
        return u
    else:
        u = u + recursive(v)
        return u


print('result:', recursive(input_string))
