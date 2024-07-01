def solution(A):
    max_ending = 0
    max_sum = 0

    for i in range(0, len(A)):
        max_ending = max(0, max_ending + A[i])
        max_sum = max(max_sum, max_ending)

    if max_sum == 0:
        return max(A)
    return max_sum


print(solution([3, 2, -6, 4, 0]))
print(solution([3, 2, -1, 30, 0]))
print(solution([1]))
print(solution([-100, -100]))
print(solution([-100, -200, 300]))
print(solution([-200, -100, -50]))
print(solution([100, -50, 10000]))
print(solution([-1, 2]))
print(solution([-10]))