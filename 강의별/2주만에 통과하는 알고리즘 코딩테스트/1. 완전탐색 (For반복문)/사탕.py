n = int(input())

a_count = 0
b_count = 0
c_count = 0

total = 0

for a in range(3, n + 1):
    a_count = a
    b_count = a_count - 2
    for c in range(2, n - a_count - b_count + 1, 2):
        c_count = c
        total += 1
        # print(a_count, b_count, c_count)

print(total)