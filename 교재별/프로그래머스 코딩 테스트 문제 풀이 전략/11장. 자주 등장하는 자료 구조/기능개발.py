from collections import deque


def solution(progresses, speeds):
    answer = []

    queue = deque()
    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] == 0:
            queue.append((100 - progresses[i]) // speeds[i])
        else:
            queue.append((100 - progresses[i]) // speeds[i] + 1)

    cnt = 1
    c1 = queue.popleft()

    while queue:
        c2 = queue.popleft()
        if c2 <= c1:
            cnt += 1
        else:  # c2 > c1
            answer.append(cnt)
            c1 = c2
            cnt = 1

    answer.append(cnt)
    return answer