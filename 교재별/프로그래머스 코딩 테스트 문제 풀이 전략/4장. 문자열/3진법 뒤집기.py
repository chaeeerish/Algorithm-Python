def solution(n):
    진법_결과 = []
    몫 = n
    while 몫 != 0:
        몫, 나머지 = divmod(몫, 3)
        진법_결과.insert(0, 나머지)

    return sum(value * (3 ** i) for i, value in enumerate(진법_결과))

# 7
print(solution(45))
# 229
print(solution(125))