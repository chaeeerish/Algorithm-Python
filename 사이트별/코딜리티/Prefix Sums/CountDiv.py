def solution(A, B, K):
    if B % K == 0 and A % K == 0:
        return (B // K) - (A // K) + 1
    elif B % K == 0 and A % K != 0:
        return (B // K) - (A // K)
    elif B % K != 0 and A % K == 0:
        return (B // K) - (A // K) + 1
    else:
        return (B // K) - (A // K)


print(solution(6, 11, 2)) # 3
print(solution(6, 7, 2)) # 1
print(solution(6, 12, 3)) # 3
print(solution(5, 7, 6)) # 1
print(solution(31, 37, 2)) # 3
print(solution(1, 1000000000, 2)) # 50000000
print(solution(1, 2, 2)) # 1