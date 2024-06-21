def solution(A):
    if set(A) == set([n for n in range(1, len(A) + 1)]):
        return 1
    else:
        return 0

print(solution([4, 1, 3, 2]))
print(solution([4, 1, 3]))

print(solution([2, 1]))

array = [n for n in range(1, 100000)]
array.reverse()
print(solution(array))
