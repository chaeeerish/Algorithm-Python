"""
4
1 3 1 5
"""

n = int(input())
array = list(map(int, input().split()))
total = [-1] * n

def get_max(i):
    if i >= n or i < 0:
        return 0

    if total[i] != -1:
        return total[i]
    else:
        total[i] = max(get_max(i-1), array[i] + get_max(i-2))
        return total[i]

print(get_max(n-1))