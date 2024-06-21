def solution(A):
    A.sort()
    i = 0
    while i + 1 < len(A):
        if A[i] == A[i + 1]:
            i += 2
        else:
            return A[i]
    return A[-1]
