import math


def reverse(b):
    if b == '0':
        return '1'
    elif b == '1':
        return '0'


def solution(numbers):
    answer = []

    for number in numbers:
        cand = math.inf

        bin_number = format(number, 'b')
        bin_number = '0' * (50 - len(bin_number)) + bin_number

        # 1개 다른 경우
        for i in range(len(bin_number) - 1, -1, -1):
            new_bin = int('0b' + bin_number[:i] + str(int(bin_number[i]) ^ 1) + bin_number[i + 1:], 2)
            if new_bin > cand:
                break
            if new_bin > number and new_bin < cand:
                cand = new_bin
                break

        for a in range(49, -1, -1):
                b = a - 1
                new_bin = int('0b' + bin_number[:b] + str(int(bin_number[b]) ^ 1) + bin_number[b + 1:a] + str(int(bin_number[a]) ^ 1) + bin_number[a + 1:], 2)
                if new_bin > cand:
                    break
                if new_bin < cand and new_bin > number:
                    cand = new_bin

        answer.append(cand)

    return answer

print(solution([2, 7])) # [3, 11]