def solution(A):
    if len(A) == 0:
        return 1

    A.sort()
    A.insert(0, 0)

    for i in range(1, len(A)):
        if i != A[i]:
            return i

    return len(A)

print(solution([]))
print(solution([1]))
print(solution([1, 3]))
print(solution([1, 2, 4]))
print(solution([n for n in range(1, 100000)] + [100000]))
