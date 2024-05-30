n, m = map(int, input().split())
a = list(map(int, input().split()))

def 자르면_몇cm(array, cut):
    new_array = []

    for i in range(len(array)):
        if array[i] - cut < 0:
            new_array.append(0)
        else:
            new_array.append(array[i] - cut)

    return sum(new_array)

result = 0
start = 0
end = max(a)

while(start <= end):
    mid = (start + end) // 2

    total = 자르면_몇cm(a, mid)
    if total < m:
        end = mid - 1
    elif total == m:
        result = mid
        break
    else: # total > m
        result = mid
        start = mid + 1

print(result)
