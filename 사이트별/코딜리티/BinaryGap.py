'''
양의 정수 n내의 binary gap = 연속적인 0들의 최대 시퀀스다.
9 => 1001 => 2
529 => 1000010001 => 4, 3
20 => 10100 => 1
15 => 1111 => X

input: N
output: its longest binary gap
'''

def solution(N):
    string = str(bin(N))[2:] # 1000010001

    max_0 = -1
    count = 0
    for i in range(len(string)):
        if string[i] == '1':
            max_0 = max(max_0, count)
            count = 0
        else:
            count += 1
    return max_0

# print(solution(1041))
# print(solution(15))
# print(solution(32))
print(solution(2147483647))