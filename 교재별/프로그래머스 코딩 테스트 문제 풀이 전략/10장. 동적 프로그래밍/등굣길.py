import math


def bfs(x, y, m, n, puddles, cur_path, min_path):
    if [y, x] in puddles:
        return 0

    if (y == n - 1 and x == m) or (y == n and x == m - 1):
        if cur_path == min_path:
            return 1
        else:
            return 0

    if y > n or x > m:
        return 0

    return bfs(x, y + 1, m, n, puddles, cur_path + 1, min_path) + bfs(x + 1, y, m, n, puddles, cur_path + 1, min_path)


def solution(m, n, puddles):
    path = [[0] * (m + 1) for _ in range(n + 1)]

    for k in range(len(puddles)):
        if len(puddles[k]) != 0:
            puddles[k] = [puddles[k][1], puddles[k][0]]

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if i == 1 and j == 1:
                continue
            if [i, j] in puddles:
                path[i][j] = math.inf
                continue

            if i == 1:
                path[i][j] = path[i][j - 1] + 1
                continue
            if j == 1:
                path[i][j] = path[i - 1][j] + 1
                continue

            path[i][j] = min(path[i - 1][j], path[i][j - 1]) + 1

    min_path = min(path[n - 1][m], path[n][m - 1])
    cnt = bfs(1, 1, m, n, puddles, 0, min_path)
    return cnt % 1000000007