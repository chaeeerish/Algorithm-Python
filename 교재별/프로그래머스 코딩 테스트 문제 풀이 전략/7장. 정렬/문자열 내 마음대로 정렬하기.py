def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))

# ["car", "bed", "sun"]
print(solution(["sun", "bed", "car"], 1))
# ["abcd", "abce", "cdx"]
print(solution(["abce", "abcd", "cdx"], 2))