def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]

    for row in range(len(arr1)):
        for col in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[row][col] += arr1[row][k] * arr2[k][col]
    return answer

# [[15, 15], [15, 15], [15, 15]]
print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
# [[22, 22, 11], [36, 28, 18], [29, 20, 14]]
print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))