def solution(n):
    피보나치 = [0, 1]
    for i in range(2, n + 1):
        피보나치.append(피보나치[i - 2] + 피보나치[i - 1])

    return 피보나치[-1] % 1234567