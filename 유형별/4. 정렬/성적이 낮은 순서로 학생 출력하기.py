'''
2
홍길동 95
이순신 77
'''

n = int(input())
array = []

for _ in range(n):
    name, score = input().split()
    score = int(score)

    array.append((name, score))

array.sort(key=lambda x:x[1])

for a in array:
    print(a[0], end=" ")