import math


def solution(stones, k):
    answer = math.inf

    left = 0
    right = k * max(stones)
    while left <= right:
        mid = (left + right) // 2

        consecutive = 0
        for stone in stones:
            if stone <= mid:
                consecutive += 1
            else:
                consecutive = 0

            if consecutive >= k:
                break

        if consecutive >= k:
            right = mid - 1
            answer = min(answer, mid)
        else:
            left = mid + 1

    if answer == math.inf:
        return 0
    return answer

# 3
print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))