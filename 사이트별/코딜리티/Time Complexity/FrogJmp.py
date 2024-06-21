def solution(X, Y, D):
    count = ((Y - X) // D)
    if ((Y - X) % D) == 0:
        return count
    return count + 1

print(solution(10, 85, 30))
print(solution(0, 90, 30))
print(solution(1, 1, 5))