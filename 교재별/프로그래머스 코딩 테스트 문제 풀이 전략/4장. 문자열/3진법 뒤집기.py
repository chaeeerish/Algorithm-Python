def solution(n):
    진법_결과 = []
    몫 = n
    while 몫 != 0:
        몫, 나머지 = divmod(몫, 3)
        진법_결과.insert(0, 나머지)

    answer = 0
    for i in range(len(진법_결과)):
        answer += 진법_결과[i] * (3 ** i)
    return answer

# 7
print(solution(45))
# 229
print(solution(125))