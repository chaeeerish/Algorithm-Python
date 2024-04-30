'''
3
15
27
12
'''

n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

sorted_list = sorted(array, reverse=True)
for i in sorted_list:
    print(i, end=" ")