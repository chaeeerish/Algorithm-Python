def solution(answers):
    수포자_리스트 = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    수포자_정답수 = [0, 0, 0]

    for j in range(len(answers)):
        for i in range(len(수포자_리스트)):
            if answers[j] == 수포자_리스트[i][j % len(수포자_리스트[i])]:
                수포자_정답수[i] += 1

    return [i + 1 for i in range(len(수포자_정답수)) if 수포자_정답수[i] == max(수포자_정답수)]

# [1]
print(solution([1, 2, 3, 4, 5]))
# [1, 2, 3]
print(solution([1, 3, 2, 4, 2]))