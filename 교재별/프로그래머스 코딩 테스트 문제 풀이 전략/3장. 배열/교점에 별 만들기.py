# -*- coding: utf-8 -*-
import math


def solution(line):
    coordinates = []
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            if (line[i][0] * line[j][1]) - (line[i][1] * line[j][0]) != 0:
                x = ((line[i][1] * line[j][2]) - (line[i][2] * line[j][1])) / (
                        (line[i][0] * line[j][1]) - (line[i][1] * line[j][0]))
                y = ((line[i][2] * line[j][0]) - (line[i][0] * line[j][2])) / (
                        (line[i][0] * line[j][1]) - (line[i][1] * line[j][0]))
            if int(x) == x and int(y) == y:
                coordinates.append((int(x), int(y)))

    min_x, max_x = min(coordinates, key=lambda x : x[0])[0], max(coordinates, key=lambda x : x[0])[0]
    min_y, max_y = min(coordinates, key=lambda x : x[1])[1], max(coordinates, key=lambda x : x[1])[1]
    mid_x = (min_x + max_x) // 2
    mid_y = (min_y + max_y) // 2

    stars = [["."] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]
    for coordinate in coordinates:  # (4, 0)
        # print(coordinate)
        # print(coordinate[0] - min_x)
        # print(max_y - coordinate[1])
        stars[max_y - coordinate[1]][coordinate[0] - min_x] = "*"

    return [''.join(star) for star in stars]


# ["....*....", ".........", ".........", "*.......*", ".........", ".........", ".........", ".........", "*.......*"]
print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
# ["*.*"]
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
# ["*"]
print(solution([[1, -1, 0], [2, -1, 0]]))
# ["*"]
print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))