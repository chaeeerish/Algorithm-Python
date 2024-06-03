def solution(s):
    answer = [0, 0] # 이진 변환의 횟수, 제거된 0의 개수

    while s != '1':
        answer[0] += 1

        # x의 모든 0을 제거한다.
        result = ''.join([char for char in s if char == '1'])
        answer[1] += sum(1 for char in s if char != '1')
        s = result

        # c를 2진법으로 표현한 문자열
        s = bin(len(s))[2:]

    return answer

# [3, 8]
print(solution("110010101001"))
# [3, 3]
print(solution("01110"))
# [4, 1]
print(solution("1111111"))