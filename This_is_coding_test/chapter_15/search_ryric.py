from bisect import bisect_left, bisect_right


def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


# 거꾸로 된 배열과 그대로 받은 배열 만들기
# for문안에서 뒤집으면서 sort 시키면 n^2logn이 나오므로 미리 만들어 놓기
array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]


def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word)
        # 문자열 뒤집기 word[::-1]
        reversed_array[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    for q in queries:
        if q[0] != '?':
            res = count_by_range(array[len(q)], q.replace(
                '?', 'a'), q.replace('?', 'z'))
        else:
            res = count_by_range(
                reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        answer.append(res)
    return answer
