import math


def solution(N):
    perimeter = math.inf

    for n in range(1, int(math.sqrt(N)) + 1):
        if N % n == 0:
            perimeter = min(perimeter, 2 * (n + (N // n)))

    return perimeter

print(solution(30))
print(solution(1))