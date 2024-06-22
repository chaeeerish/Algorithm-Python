def solution(A):
    a = set([n for n in range(2, max(A) + 2)] + [1]) - set(A)
    return min(a)


def solution(A):
    last_positive = 0

    A.sort()
    for n in A:
        if n <= 0:
            continue
        else:
            if n == last_positive + 1:
                last_positive += 1
            elif n > last_positive + 1:
                break
            else: # n <= last_positive
                last_positive = n

    return last_positive + 1


# print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 2, 3]))
print(solution([-1, -3]))
print(solution([1]))
print(solution([0]))
print(solution([1000000]))
