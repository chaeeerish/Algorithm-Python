import math


def solution(n, k):
    answer = []
    사람_리스트 = [i for i in range(1, n + 1)]

    for i in range(n):
        index = 1
        while True:
            팩토리얼_값 = math.factorial(len(사람_리스트) - 1) * index
            if 팩토리얼_값 >= k:
                k -= math.factorial(len(사람_리스트) - 1) * (index - 1)
                answer.append(사람_리스트[index - 1])
                del 사람_리스트[index - 1]
                break
            else: # 팩토리얼_값 <= k
                index += 1

    return answer


print(solution(5, 3)) # [1, 2, 4, 3, 5]
print(solution(3, 5)) # [3, 1, 2]