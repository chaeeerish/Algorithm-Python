import math


def get_k진수(n, k):
    answer = ''
    while n:
        answer += str(n % k)
        n //= k
    return answer[::-1]


def is_소수(n):
    if n == 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0

    result = get_k진수(n, k)
    for str1 in result.split("0"):
        if str1 and is_소수(int(str1)):
            answer += 1

    return answer