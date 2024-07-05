import math


def operate(A, B, operate):
    if operate == '+':
        return A + B
    elif operate == '-':
        return A - B
    elif operate == '*':
        return A * B
    elif operate == '//' and B != 0:
        return A // B
    else:
        return -1


def dp(N, number, current, cnt):
    if cnt > 8:
        return math.inf

    if current == number:
        return cnt
    elif current < 0:
        return math.inf

    candidate = []
    operations = ['+', '-', '*', '//']

    for i in range(1, len(str(number)) + 1):
        N_new = int(str(N) * i)
        for j in range(4):
            candidate.append(dp(N, number, operate(current, N_new, operations[j]), cnt + i))

    return min(candidate)


def solution(N, number):
    answer = dp(N, number, 0, 0)
    if answer == math.inf:
        return -1
    return answer


# print(solution(5, 12)) # 4
# print(solution(5, 31168)) # -1
# print(solution(2, 11)) # 3
# print(solution(1, 1))
# print(solution(3, 333))
print(solution(4, 31)) # 3
print(solution(1, 121)) # 4
print(solution(9, 0)) # 2
print(solution(1, 37))