def solution(n, times):
    left = 1
    right = max(times) * n

    while left <= right:
        mid = (left + right) // 2
        people = 0

        for time in times:
            people += mid // time

            if people >= n:
                break

        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

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