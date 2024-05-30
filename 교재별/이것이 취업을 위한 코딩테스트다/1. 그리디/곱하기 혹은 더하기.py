S = input()
array = list(map(int, S))

result = array[0]
index = 1

while True:
    if index >= len(array):
        break
    result = max(result * array[index], result + array[index])
    index += 1

print(result)
