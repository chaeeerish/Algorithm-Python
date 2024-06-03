import math


def solution(rows, columns, queries):
    cnt = 1
    maps = [[cnt + col + row * columns for col in range(columns)] for row in range(rows)]

    answer = []
    for query in queries:
        x1 = query[0] - 1
        y1 = query[1] - 1
        x2 = query[2] - 1
        y2 = query[3] - 1
        minNum = math.inf

        # 1
        previous = maps[x1][y1]
        for col in range(y1 + 1, y2 + 1):
            next = maps[x1][col]
            maps[x1][col] = previous
            previous = next
            minNum = min(minNum, maps[x1][col])

        # for i in range(rows):
        #     for j in range(columns):
        #         print(maps[i][j], end="\t")
        #     print()
        # print()

        # 2
        for row in range(x1 + 1, x2 + 1):
            next = maps[row][y2]
            maps[row][y2] = previous
            previous = next

            minNum = min(minNum, maps[row][y2])

        # 3
        for col in range(y2 - 1, y1 - 1, -1):
            next = maps[query[2] - 1][col]
            maps[query[2] - 1][col] = previous
            previous = next
            minNum = min(minNum, maps[query[2] - 1][col])

        # 4
        for row in range(x2 - 1, x1 - 1, -1):
            next = maps[row][query[1] - 1]
            maps[row][query[1] - 1] = previous
            previous = next
            minNum = min(minNum, maps[row][query[1] - 1])

        answer.append(minNum)

    return answer


# [8, 10, 25]
print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
# [1, 1, 5, 3]
print(solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]))
# [1]
print(solution(100, 97, [[1, 1, 100, 97]]))
