def tower_of_hanoi(answer, m, a, b, c): # a에 있는 m개의 원판을 b를 이용해서 c로 옮긴다.
    if m == 2:
        answer.extend([[a, b], [a, c], [b, c]])
        return answer
    else:
        answer = tower_of_hanoi(answer, m - 1, a, c, b)
        answer.append([a, c])
        answer = tower_of_hanoi(answer, m - 1, b, a, c)

    return answer

def solution(n):
    answer = []
    return tower_of_hanoi(answer, n, 1, 2, 3)

# [[1, 2], [1, 3], [2, 3]]
print(solution(2))