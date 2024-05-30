'''
5
8 3 7 9 2
3
5 7 9
'''

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

for temp in b:
    if temp in a:
        print("yes", end=" ")
    else:
        print("no", end=" ")