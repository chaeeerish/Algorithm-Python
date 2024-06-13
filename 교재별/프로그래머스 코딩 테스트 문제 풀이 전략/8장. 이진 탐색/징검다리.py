import itertools

def get_new_바위_사이_리스트(바위_사이_리스트, 제외할_바위):
    new_바위_사이_리스트 = []

    i = 0
    while i < len(바위_사이_리스트):
        if i not in 제외할_바위:
            new_바위_사이_리스트.append(바위_사이_리스트[i])
        else:
            new_바위_사이_리스트.append(바위_사이_리스트[i] + 바위_사이_리스트[i + 1])
            i += 1
        i += 1

    return new_바위_사이_리스트

def solution(distance, rocks, n):
    rocks.sort()

    바위_사이_리스트 = []
    바위_사이_리스트.append(rocks[0])
    for i in range(len(rocks) - 1):
        바위_사이_리스트.append(rocks[i + 1] - rocks[i])
    바위_사이_리스트.append(distance - rocks[-1])

    최소_거리 = -1
    # rock의 길이(5) 중에 2개 고르기
    for iter in itertools.combinations([i for i in range(len(rocks))], n):
        new_바위_사이_리스트 = get_new_바위_사이_리스트(바위_사이_리스트, iter)
        최소_거리 = max(최소_거리, min(new_바위_사이_리스트))

    return 최소_거리

# 0 2 11 14 17 21 25
#  2 9  3  3  4  4
# 2개 제거 하면 -> 바위 사이의 거리 리스트에서도 2개가 제거된다
# 2 9 3 11 - [17, 21] 제거
# 11 3 3 8 - [2, 21] 제거
# 4
print(solution(25, [2, 14, 11, 21, 17], 2))