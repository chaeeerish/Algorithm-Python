import itertools


def solution(A):
    count_0 = 0
    count_1 = 0

    result = 0
    for i in range(len(A)):
        if A[i] == 0:
            count_0 += 1
        else:
            count_1 += 1
            result += count_0
            if result > 1000000000:
                result = -1
                break
    return result


print(solution([0, 1, 0, 1, 1]))
print(solution([1, 0]))