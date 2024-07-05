def solution(m, n, puddles):
    path = [[0] * (m + 1) for _ in range(n + 1)]

    for k in range(len(puddles)):
        if len(puddles[k]) != 0:
            puddles[k] = [puddles[k][1], puddles[k][0]]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if [i, j] in puddles:
                continue

            if i == 1 and j == 1:
                path[i][j] = 1
            elif i == 1:
                path[i][j] = path[i][j - 1]
            elif j == 1:
                path[i][j] = path[i - 1][j]
            else:
                path[i][j] = path[i - 1][j] + path[i][j - 1]

    return path[n][m] % 1000000007