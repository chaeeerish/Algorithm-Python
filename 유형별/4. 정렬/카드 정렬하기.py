import heapq

n = int(input()) # 최대 100,000
hq = []

for _ in range(n):
    heapq.heappush(hq, int(input()))

total = 0

if len(hq) == 1:
    print(0)
else:
    i = 0
    while True:
        if len(hq) == 1:
            print(total)
            break

        sum = heapq.heappop(hq) + heapq.heappop(hq)
        total += sum

        heapq.heappush(hq, sum)

"""
# 100
3
10
20
40

# 12108
10
7
12
123
234
234
455
456
876
887
998

# 24
4
3
3
3
3

# 410
4
30
40
50
100

# 0
1
100

# 80
4
10
10
10
10
"""