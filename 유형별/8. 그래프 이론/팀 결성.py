"""
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
"""
n, m = map(int, input().split())
parent = [-1] * (n + 1)

for i in range(0, n + 1):
    parent[i] = i

def combine(a, b):
    a = parent[a]
    b = parent[b]
    if a < b:
        parent[b] = a

def check_same_team(a, b):
    if parent[a] != parent[b]:
        print('NO')
    else:
        print('YES')

for _ in range(m):
    cal, a, b = map(int, input().split())
    if cal == 0:
        combine(a, b)
    elif cal == 1:
        check_same_team(a, b)
