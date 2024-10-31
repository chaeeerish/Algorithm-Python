n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

answer = []
for i in range(n):
    flag = True
    for j in range(2, 1000000):
        if array[i] % j == 0:
                flag = False
                break

    if flag:
        answer.append("YES")
    else:
        answer.append("NO")

for i in range(n):
    print(answer[i])