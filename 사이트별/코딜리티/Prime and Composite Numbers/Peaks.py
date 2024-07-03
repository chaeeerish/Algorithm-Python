def solution(A):
    peaks = []
    for i in range(1, len(A) - 1):
        if A[i] > A[i - 1] and A[i] > A[i + 1]:
            peaks.append(i)

    if len(peaks) == 0:
        return 0
    elif len(peaks) == 1:
        return 1

    for i in range(len(peaks), 0, -1):
        if len(A) % i == 0:
            block_size = len(A) // i
            blocks = [False] * i

            for j in range(len(peaks)):
                blocks[peaks[j] // block_size] = True

            if all(blocks):
                return i
    return 0


print(solution([1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2])) # 3
print(solution([1])) # 0ㅈ
print(solution([1, 2, 3, 1, 2, 4])) # 1
print(solution([1, 2, 1, 2, 1, 1])) # 2
print(solution([1, 3, 2, 1])) # 1
print(solution([1, 2, 3, 4, 1, 2, 3, 2, 5, 1])) # 2
print(solution([1, 10, 2, 10, 4, 2, 10, 1, 3])) # 3
print(solution([1, 1, 1, 2, 1, 3])) # 1
print(solution([1, 2, 1, 2, 1, 2, 1, 3, 2]))  # 3