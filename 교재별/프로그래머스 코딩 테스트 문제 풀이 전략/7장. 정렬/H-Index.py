def solution(citations):
    for i in range(max(citations), -1, -1):
        if len([j for j in range(0, len(citations)) if citations[j] >= i]) >= i:
            return i
    return len(citations)

# 3
print(solution([3, 0, 6, 1, 5]))
# 0
print(solution([0, 0, 0]))
# 2
print(solution([1, 4, 5]))
# 3
print(solution([5, 6, 7]))