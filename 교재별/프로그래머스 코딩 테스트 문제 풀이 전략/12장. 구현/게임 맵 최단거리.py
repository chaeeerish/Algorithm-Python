from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(maps):
    answer = 0

    start = (0, 0)
    n = len(maps)
    m = len(maps[0])

    visited = [[False for _ in range(m)] for _ in range(n)]

    current_row = 0
    current_col = 0
    queue = deque([(current_row, current_col, 1)])
    visited[current_row][current_col] = True
    while queue:
        v = queue.popleft()

        if v[0] == n - 1 and v[1] == m - 1:
            answer = v[2]
            break

        for i in range(4):
            next_row = v[0] + dx[i]
            next_col = v[1] + dy[i]

            if 0 <= next_row < n and 0 <= next_col < m and maps[next_row][next_col] == 1 and visited[next_row][
                next_col] == False:
                visited[next_row][next_col] = True
                queue.append((next_row, next_col, v[2] + 1))

    if answer == 0:
        return -1
    return answer