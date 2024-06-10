from itertools import permutations


def is_prime_number(number):
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0

    만들_수_있는_수 = set()
    for i in range(1, len(numbers) + 1):
        for p in set(permutations(numbers, i)):
            만들_수_있는_수.add(int(''.join(p)))

    for 수 in 만들_수_있는_수:
        if is_prime_number(수):
            answer += 1

    return answer


# 3
print(solution("17"))
# 2
print(solution("011"))