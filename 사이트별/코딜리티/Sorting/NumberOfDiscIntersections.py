# def solution(A):
#     count = 0
#
#     R = []
#     for i in range(len(A)):
#         R.append((i - A[i], i + A[i]))
#
#     count = 0
#     for i in range(len(R)):
#         for j in range(i + 1, len(R)):
#             if R[i][0] <= R[j][0] <= R[i][1] or R[i][0] <= R[j][1] <= R[i][1] or R[j][0] <= R[i][0] <= R[j][1] or R[j][0] <= R[i][1] <= R[j][1]:
#                 count += 1
#                 if count > 10000000:
#                     return -1
#
#     return count


def solution(A):
    events = []
    for i, v in enumerate(A):
        events.append(((i - v), -1))
        events.append(((i + v), 1))
    events.sort()

    result = 0
    count = 0

    for i in range(len(events)):
        if events[i][1] == 1:
            count -= 1
        elif events[i][1] == -1:
            result += count
            count += 1

        if result > 10000000:
            return -1
    return result

print(solution([1, 5, 2, 1, 4, 0]))