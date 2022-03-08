from collections import deque


def solution(N, stages):
    answer = []
    stages.sort()

    # 1~N까지는 실패율
    # N+1은 다 성공한사람
    failure_rate = [0 for _ in range(N+2)]

    # 사용할 변수 초기화
    prev = stages[0]
    count = 0
    length = len(stages)

    q = deque(stages)
    while q:
        v = q.popleft()
        # if v == N+1:
        #    failure_rate[v] += 1
        # print('----------')
        # print('v:',v)
        #print('prev:', prev)
        if prev != v:
            #print('count:', count)
            #print('length q:', length)
            #print('value: ', count / length)
            failure_rate[prev] = count / length
            for _ in range(count):
                length -= 1
            #print('after length q:', length)
            count = 0
            prev = v
        count += 1
        #print('count:', count)
    #print(' out v:', v)
    # 마지막에 처리 안된 것을 작업
    failure_rate[v] = count / length

    result = []
    for i in range(1, N+1):
        result.append((failure_rate[i], i))
    result.sort(key=lambda x: (-x[0], x[1]))
    print(result)

    for _, stage in result:
        answer.append(stage)
    return answer
