def solution(A):
    if len(A) == 0:
        return -1

    value = A[0]
    size = 1

    for i in range(1, len(A)):
        if size == 0:
            value = A[i]
            size = 1
        else:
            if value != A[i]:
                size -= 1
            else:
                size += 1

    if size > 0:
        answer = []
        for i in range(len(A)):
            if A[i] == value:
                answer.append(i)
        if len(answer) > (len(A) // 2):
            return answer[0]
    return -1

print(solution([]))
print(solution([1]))
print(solution([3, 4, 3, 2, 3, -1, 3, 3]))
print(solution([1, 1, 1, 1, 2, 2, 2, 2]))
print(solution([0, 0, 0, 1, 1, 1, 1]))
print(solution([1, 1, 1, 2, 2, 2]))