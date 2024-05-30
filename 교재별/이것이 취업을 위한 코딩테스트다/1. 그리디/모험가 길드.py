"""
5
2 3 1 2 2
"""
n = int(input())
array = list(map(int, input().split()))

array.sort(reverse=True)

count = 0
i = 0

while True:
    if i >= len(array):
        break

    if (i + array[i] - 1) > len(array) - 1:
        break
    else:
        count += 1
        i = i + array[i]

print(count)
