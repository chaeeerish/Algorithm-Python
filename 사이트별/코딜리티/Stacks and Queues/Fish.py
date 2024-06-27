from collections import deque


def solution(A, B):
    queue = deque()

    for i in range(0, len(A)):
        if B[i] == 1:
            queue.append((B[i], A[i]))
        else: # B[i] == 0:
            queue.append((B[i], A[i]))
            j = len(queue) - 1
            while 0 <= j <= len(A) - 1:
                if queue[j - 1][0] == 1:
                    elem_j = queue.pop()
                    elem_j_1 = queue.pop()
                    if elem_j[1] > elem_j_1[1]:
                        queue.append(elem_j)
                        j -= 1
                    else:
                        queue.append(elem_j_1)
                        break
                else: # queue[j - 1][0] == 0:
                    break

    return len(queue)


print(solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]))
print(solution([5, 6], [0, 1]))
print(solution([5, 6], [1, 0]))
print(solution([1, 2, 3, 4, 5], [0, 0, 0, 0, 0]))