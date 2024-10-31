A = int(input())
B = []

for _ in range(A):
    a, b, c = map(int, input().split())
    B.append((a, b, c))

def get_strike_ball(A, B):
    A = str(A)
    B = str(B)

    strike = 0
    ball = 0

    for i in range(3):
        if A[i] == B[i]:
            strike += 1
        else:
            if A[i] in B[:i] + B[i + 1:]:
                ball += 1

    return strike, ball

for a in range(100, 999):
    if a in [111, 222, 333, 444, 555, 666, 777, 888, 999]:
        continue

    flag = 0
    for b, strike, ball in B:
        cur_strike, cur_ball = get_strike_ball(a, b)
        if cur_strike == strike and cur_ball == ball:
            flag += 1
        else:
            break
    if flag == len(B):
        print(a)
        break