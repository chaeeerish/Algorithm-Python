def solution(A):
    value = A[0]
    size = 1
    for i in range(1, len(A)):
        if size == 0:
            size = 1
            value = A[i]
        else:
            if value != A[i]:
                size -= 1
            else:
                size += 1

    if size > 0:
        full_count = 0
        answer = 0
        for i in range(0, len(A)):
            if A[i] == value:
                full_count += 1

        if full_count > len(A) // 2:
            left_count = 0
            right_count = 0
            for i in range(len(A) - 1):
                if A[i] == value:
                    left_count += 1
                    right_count = full_count - left_count

                if left_count > ((i + 1) // 2) and right_count > ((len(A) - (i + 1)) // 2):
                    # print("left_count =", left_count, "right_count =", right_count, "i =", i)
                    answer += 1
        return answer
    return 0


print(solution([4, 3, 4, 4, 4, 2]))
print(solution([1]))
print(solution([1, 1]))
print(solution([1, 2]))
print(solution([1, 2, 1, 2, 1, 1]))