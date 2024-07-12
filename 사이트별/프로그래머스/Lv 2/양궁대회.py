import math
from collections import deque


def 점수_계산(라이언, 어피치):
    라이언_점수 = 0
    어피치_점수 = 0

    for i in range(11):
        if 라이언[i] > 어피치[i]:
            라이언_점수 += (10 - i)
        elif 라이언[i] < 어피치[i]:
            어피치_점수 += (10 - i)
        else:  # 라이언[i] == 어피치[i]:
            if 라이언[i] == 0 and 어피치[i] == 0:
                continue
            else:
                어피치_점수 += (10 - i)

    return (라이언_점수 - 어피치_점수)


def solution(n, info):
    answer = []

    queue = deque()
    라이언 = [0] * 11
    남은_화살 = n
    queue.append((라이언, 0, 남은_화살))

    while queue:
        라이언, 현재_인덱스, 남은_화살 = queue.popleft()

        # print("라이언 = ", 라이언)
        # print("현재_인덱스 = ", 현재_인덱스)
        # print("남은_화살 = ", 남은_화살)
        # print()

        # 종료 조건
        if 남은_화살 == 0:
            if 현재_인덱스 == 11:
                answer.append(라이언)
                continue
            else:
                answer.append(라이언)
                continue
        else:  # 남은_화살 != 0
            if 현재_인덱스 == 11:
                라이언[10] += 남은_화살
                answer.append(라이언)
                continue

        # 지는 경우
        지는_라이언 = 라이언[:]
        queue.append((지는_라이언, 현재_인덱스 + 1, 남은_화살))

        # 이기는 경우
        이기는_라이언 = 라이언[:]
        if info[현재_인덱스] + 1 <= 남은_화살:
            이기는_라이언[현재_인덱스] = info[현재_인덱스] + 1
            queue.append((이기는_라이언, 현재_인덱스 + 1, 남은_화살 - (info[현재_인덱스] + 1)))

    if len(answer) == 0:
        return [-1]

    flag = True
    for a in answer:
        if a[0] >= 1:
            flag = False
            break

    if flag == True:
        return [-1]

    중복_제거_answer = [list(t) for t in set(tuple(l) for l in answer)]

    정렬_answer = []
    for a in 중복_제거_answer:
        정렬_answer.append((점수_계산(a, info), a))
    정렬_answer.sort(reverse=True)

    if 정렬_answer[0][0] == 0:
        return [-1]

    최대_차이 = 정렬_answer[0][0]
    최대_차이_answer = []
    for a in 정렬_answer:
        if a[0] == 최대_차이:
            최대_차이_answer.append(a[1])

    for i in range(10, -1, -1):
        min_index = 0
        min_count = math.inf
        for j in range(len(최대_차이_answer)):
            if 최대_차이_answer[j][i] == min_count:
                min_count = math.inf
                break
            if 최대_차이_answer[j][i] > 0 and 최대_차이_answer[j][i] < min_count:
                min_count = 최대_차이_answer[j][i]
                min_index = j

        if min_count != math.inf:
            return 최대_차이_answer[min_index]

    return 최대_차이_answer


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0])) # [0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0]
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])) # [-1]
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1])) # [1, 1, 2, 0, 1, 2, 2, 0, 0, 0, 0]
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3])) # [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 2]