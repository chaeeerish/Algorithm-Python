"""
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2

5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2

5 1
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0

5 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
"""
n, m = map(int, input().split())

city = []

for _ in range(n):
    city.append(list(map(int, input().split())))

total_chicken = 0
for i in range(n):
    total_chicken += city[i].count(2)

house = dict()
chicken = dict()
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house[(i, j)] = dict()
        elif city[i][j] == 2:
            chicken[(i, j)] = 0

for h_key in house.keys():
    for c_key in chicken.keys():
        distance = abs(h_key[0] - c_key[0]) + abs(h_key[1] - c_key[1])
        house[h_key][c_key] = distance
        chicken[c_key] += distance
    house[h_key] = dict(sorted(house[h_key].items(), key=lambda item: item[1]))
chicken = dict(sorted(chicken.items(), key=lambda item: item[1]))

for _ in range(total_chicken - m):
    maximum = chicken.popitem()
    for h_key in house.keys():
        del house[h_key][maximum[0]]

# 도시의 최소 치킨 거리
minimum = 0
for h_key in house.keys():
    minimum += min(house[h_key].values())

print(minimum)
