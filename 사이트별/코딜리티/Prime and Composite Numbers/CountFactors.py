import math


def solution(N):
    cnt = 0
    for d in range(1, int(math.sqrt(N)) + 1):
        if N % d == 0:
            if N // d == math.sqrt(N):
                cnt += 1
            else:
               cnt += 2
    return cnt


print(solution(24))
print(solution(9))
print(solution(1))
print(solution(36))
print(solution(100))