def solution(N, stages):
    스테이지에_있는_플레이어_수 = [0] * (N + 2)
    스테이지를_거쳐간_플레이어_수 = [0] * (N + 2)

    for i in range(len(stages)):
        스테이지에_있는_플레이어_수[stages[i]] += 1
        for j in range(1, stages[i] + 1):
            스테이지를_거쳐간_플레이어_수[j] += 1

    실패율_내림차순 = []
    for i in range(1, N + 1):
        실패율 = 0
        if 스테이지를_거쳐간_플레이어_수[i] != 0:
            실패율 = 스테이지에_있는_플레이어_수[i] / 스테이지를_거쳐간_플레이어_수[i]
        실패율_내림차순.append((i, 실패율))

    실패율_내림차순.sort(key=lambda x: (x[1], -x[0]), reverse=True)

    return [x[0] for x in 실패율_내림차순]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
