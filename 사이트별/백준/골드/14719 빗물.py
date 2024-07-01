h, w = map(int, input().split())
array = list(map(int, input().split()))

if len(array) <= 2 or w == 0:
    print(0)
else:
    candidate = []
    if array[0] >= array[1]:
        candidate.append(0)

    for i in range(1, len(array) - 1):
        if array[i - 1] <= array[i] and array[i + 1] <= array[i]:
                candidate.append(i)

    if array[-1] >= array[-2]:
        candidate.append(len(array) - 1)

    # print(candidate)

    j = 1
    while True:
        if j >= len(candidate) - 1:
            break

        flag1 = False
        for k in range(0, j):
            if array[candidate[j]] <= array[candidate[k]]:
                flag1 = True

        flag2 = False
        for k in range(j + 1, len(candidate)):
            if array[candidate[j]] <= array[candidate[k]]:
                flag2 = True

        if flag1 and flag2:
            del candidate[j]
        else:
            j += 1

    # print(candidate)
    # print(array)

    result = 0
    for i in range(len(candidate) - 1):
        for j in range(candidate[i] + 1, candidate[i + 1]):
            temp = min(array[candidate[i]], array[candidate[i + 1]]) - array[j]
            if temp > 0:
                result += temp
    print(result)
