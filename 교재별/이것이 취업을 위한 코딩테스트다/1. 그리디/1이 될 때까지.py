n, k = map(int, input().split())

number = 0

while True:
    if n == 1:
        break

    if n % k == 0:
        n = n / k
        number += 1
    else:
        n -= 1
        number += 1

print(number)