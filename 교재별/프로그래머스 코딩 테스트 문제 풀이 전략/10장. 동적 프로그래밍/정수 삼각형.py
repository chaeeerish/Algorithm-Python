def solution(triangle):
    flag = [[False] * len(triangle[i]) for i in range(len(triangle))]

    for j in range(len(triangle[-1])):
        flag[-1][j] = triangle[-1][j]

    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            flag[i][j] = max(flag[i + 1][j], flag[i + 1][j + 1]) + triangle[i][j]

    return flag[0][0]

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])) # 30