def solution(H):
    blockCount = 0
    blockStack = []

    for i in range(len(H)):
        while blockStack and blockStack[-1] < H[i]:
            blockStack.pop()

        if not blockStack or blockStack[-1] > H[i]:
            blockCount += 1
            blockStack.append(H[i])

    return blockCount

print(solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))
print(solution([1]))
print(solution([1, 2, 3, 4, 5]))
print(solution([1, 1, 1, 1, 1]))
print(solution([2, 1, 1, 1, 1, 2]))