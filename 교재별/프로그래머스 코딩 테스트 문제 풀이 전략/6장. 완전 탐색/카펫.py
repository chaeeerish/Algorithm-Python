def solution(brown, yellow):
    for a in range(1, 5000):
        for b in range(1, 5000):
            if a * b == brown + yellow and a + b == (brown + 4) // 2 and (a - 2) * (b - 2) == yellow:
                return sorted([a, b], reverse=True)

# [4, 3]
print(solution(10, 2))
# [3, 3]
print(solution(8, 1))
# [8, 6]
print(solution(24, 24))