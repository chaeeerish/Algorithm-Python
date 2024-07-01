def solution(A):
    candidate = []
    for i in range(1, len(A) - 1):
        if A[i - 1] < A[i] and A[i] > A[i + 1]:
            candidate.append(i)

    # print(candidate)

    left = 1
    right = len(candidate)
    result = 0
    while left <= right:
        if len(candidate) == 1:
            flag = [True]
        else:
            flag = [False] * len(candidate)
        mid = (left + right) // 2

        i = 0
        j = 1
        while i <= len(candidate) - 1 and j <= len(candidate) - 1:
            if abs(candidate[i] - candidate[j]) >= mid:
                flag[i] = True
                flag[j] = True
                i = j
                j = j + 1
            else:
                j = j + 1

        if flag.count(True) >= mid:
            left = mid + 1
            result = max(result, mid)
        else:
            right = mid - 1

    return result

print(solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]))
print(solution([1, 2, 3, 1, 3, 1]))
print(solution([1, 2, 1]))
print(solution([1, 2, 1, 2, 1]))