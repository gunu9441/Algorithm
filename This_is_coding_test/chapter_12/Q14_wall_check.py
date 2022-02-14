from itertools import permutations


def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    print("weak: ", weak)

    answer = len(dist) + 1

    # 0~length-1까지를 출발지로 결정
    for start in range(length):
        for friends in permutations(dist, len(dist)):
            count = 1
            position = weak[start] + friends[count-1]
            for index in range(start+1, start+length):
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count-1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1

    return answer
