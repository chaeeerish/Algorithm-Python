"""
2 15
2
3
"""

"""
3 4
3
5
7
"""

n, m = map(int, input().split())
money = []

for _ in range(n):
    money.append(int(input()))

INF = 987654321
count = [INF] * (m + 1)
count[0] = 0

def get_count(i):
    if i < 0 or i > m:
        return 0
    if count[i] == INF:
        for j in range(n):
            if i % money[j] == 0:
                count[i] = min(count[i], get_count(i - money[j]) + 1)

    return count[i]

result = get_count(m)
if result != INF:
    print(result)
else:
    print(-1)