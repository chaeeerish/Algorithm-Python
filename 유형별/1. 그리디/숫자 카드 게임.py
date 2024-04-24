n, m = map(int, input().split())

min_card = -1
max_card = 0
for i in range(n):
    data = list(map(int, input().split()))
    if min_card < min(data):
        min_card = min(data)
        max_card = max(data)

print(min_card)