import math


def 시간_계산(입국_심사대_리스트, 받은_사람들):
    return max(받은_사람들[i] * 입국_심사대_리스트[i] for i in range(len(입국_심사대_리스트)))


def 입국_심사(n, h, times, 입국_심사대_리스트):
    if n == 0 and h == 0:
        return 시간_계산(times, 입국_심사대_리스트)
    elif n != 0 and h == 0:
        return math.inf
    elif n == 0 and h != 0:
        return 시간_계산(times, 입국_심사대_리스트 + ([0] * h))

    최소_시간 = math.inf
    for i in range(0, n + 1):
        최소_시간 = min(최소_시간, 입국_심사(n-i, h-1, times, 입국_심사대_리스트 + [i]))
    return 최소_시간


def solution(n, times):
    return 입국_심사(n, len(times), times, [])

# 28
print(solution(6, [7, 10]))
# 2
print(solution(4, [1, 1, 1]))
# 30
print(solution(59, [1, 1]))
# 40
print(solution(7, [10, 10]))
# 2
print(solution(1, [2, 2]))
# 3
print(solution(3, [1, 99, 99]))