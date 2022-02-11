def isValid(answer):
    for x, y, a in answer:
        # 기둥
        if a == 0:
            if y == 0 or [x, y-1, 0] in answer or [x-1, y, 1] in answer or [x, y, 1] in answer:
                continue
            else:
                return False
        # 보
        else:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        # 삭제
        if b == 0:
            answer.remove([x, y, a])
            if not isValid(answer):
                answer.append([x, y, a])
        else:
            answer.append([x, y, a])
            if not isValid(answer):
                answer.remove([x, y, a])
        answer.sort()
    return answer
