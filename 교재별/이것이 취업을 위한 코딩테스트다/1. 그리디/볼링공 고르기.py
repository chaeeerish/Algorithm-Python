"""
5 3
1 3 2 3 2
"""
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 내 방법
# count = 0
# for i in range(len(data)):
#     for j in range(i + 1, len(data)):
#         if data[i] != data[j]:
#             count += 1
# print(count)

# 풀이
arr = [0] * 11
for d in data:
    arr[d] += 1

result = 0
for i in range(1, m + 1):
    n -= arr[i]
    result += arr[i] * n

print(result)
