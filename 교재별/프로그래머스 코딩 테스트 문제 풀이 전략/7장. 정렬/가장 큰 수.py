def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: int((x*4)[0:4]), reverse=True)
    return str(int(''.join(numbers)))


# "6210"
print(solution([6, 10, 2]))
# "9534330"
print(solution([3, 30, 34, 5, 9]))
# "9799797881881817"
print(solution([979, 97, 978, 81, 818, 817]))
# "554754"
print(solution([547, 54, 5]))
# 0
print(solution([0, 0]))
#
print(solution([1, 10, 100, 1000, 818, 81, 898, 89, 0, 0]))
#
print(solution([328, 32]))
# "9991000
print(solution([1000, 999]))
# 23232
print(solution([232, 23]))
# 21221
print(solution([212, 21]))
# 700000
print(solution([70, 0, 0, 0, 0]))
# 10110
print(solution([101, 10]))
# "2323210110"
print(solution([101, 10, 232, 23]))