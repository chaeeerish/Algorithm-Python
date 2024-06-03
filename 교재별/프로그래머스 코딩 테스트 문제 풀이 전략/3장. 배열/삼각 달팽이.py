def solution(n):
    finalNum = 0
    for i in range(n + 1):
        finalNum += i

    array = [[0] * n for _ in range(n)]

    cnt = 1
    row = 0
    col = 0

    direction = 0 # 0: 아래 방향 1: 오른쪽 방향 2: 왼쪽 위 대각선 방향
    while True:
        array[row][col] = cnt
        cnt += 1
        if cnt > finalNum:
            break

        # 아래 방향
        if direction == 0:
            if row + 1 >= n or array[row + 1][col] != 0:
                direction = 1
                col += 1
            else:
                row += 1
        elif direction == 1:
            if col + 1 >= n or array[row][col + 1] != 0:
                direction = 2
                row -= 1
                col -= 1
            else:
                col += 1
        elif direction == 2:
            if row - 1 < 0 or col - 1 < 0 or array[row - 1][col - 1] != 0:
                direction = 0
                row += 1
            else:
                row -= 1
                col -= 1

    return [array[row][col] for row in range(len(array)) for col in range(len(array[row])) if array[row][col] != 0]

print(solution(4))
print(solution(5))
print(solution(6))