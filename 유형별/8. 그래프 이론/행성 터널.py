import sys

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

input = sys.stdin.readline
n = int(input())

x_list = []
y_list = []
z_list = []
for i in range(n):
    x, y, z = map(int, input().split())
    x_list.append((x, i))
    y_list.append((y, i))
    z_list.append((z, i))
x_list.sort()
y_list.sort()
z_list.sort()

edges = []
for i in range(n - 1):
    edges.append((abs(x_list[i + 1][0] - x_list[i][0]), x_list[i][1], x_list[i + 1][1]))
    edges.append((abs(y_list[i + 1][0] - y_list[i][0]), y_list[i][1], y_list[i + 1][1]))
    edges.append((abs(z_list[i + 1][0] - z_list[i][0]), z_list[i][1], z_list[i + 1][1]))
edges.sort()

parent = [0] * n
for i in range(n):
    parent[i] = i

result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)


"""
# 4
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
"""