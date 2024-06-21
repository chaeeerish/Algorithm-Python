def solution(N, A):
    result = [0] * N

    max_value = 0
    last_update = 0
    for i in range(len(A)):
        if 1 <= A[i] <= N:
            if result[A[i] - 1] < last_update:
                result[A[i] - 1] = last_update
            result[A[i] - 1] += 1
            if result[A[i] - 1] > max_value:
                max_value = result[A[i] - 1]
        else:
            last_update = max_value

    for i in range(len(result)):
        if result[i] < last_update:
            result[i] = last_update

    return result

print(solution(5, [3, 4, 4, 6, 1, 4, 4]))