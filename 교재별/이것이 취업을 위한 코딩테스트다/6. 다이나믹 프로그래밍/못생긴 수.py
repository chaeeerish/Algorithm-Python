import heapq

n = int(input())

array = [0, 1, 2, 3, 5]

i = 1
while True:
    i += 1

    for number in [2, 3, 5]:
        if number * array[i] not in array:
            array.append(number * array[i])

    array.sort()

    if len(array) - 1 >= n:
        print(array[n])
        break
