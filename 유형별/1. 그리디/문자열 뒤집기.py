S = input()
array = list(map(int, S))

previous = 0
count = 0

d = {0: [], 1: []}

i = 0
while True:
    if i + 1 >= len(array):
        count += 1
        d[array[i]].append(count)
        break
    if array[i] == array[i+1]:
        count += 1
    else:
        count += 1
        d[array[i]].append(count)
        count = 0
    i += 1

print(min(len(d[0]), len(d[1])))
