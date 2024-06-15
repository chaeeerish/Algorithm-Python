def solution(genres, plays):
    answer = []

    노래 = dict()
    총_재생_횟수 = dict()
    for i in range(len(genres)):
        if genres[i] in 노래:
            노래[genres[i]].append((plays[i], i))
        else:
            노래[genres[i]] = [(plays[i], i)]

        if genres[i] in 총_재생_횟수:
            총_재생_횟수[genres[i]] += plays[i]
        else:
            총_재생_횟수[genres[i]] = plays[i]

    총_재생_횟수 = sorted(총_재생_횟수.items(), key=lambda item: item[1], reverse=True)

    for i in range(len(총_재생_횟수)):
        노래[총_재생_횟수[i][0]].sort(key=lambda x: (x[0], -x[1]), reverse=True)
        if len(노래[총_재생_횟수[i][0]]) == 1:
            answer.append(노래[총_재생_횟수[i][0]][0][1])
        elif len(노래[총_재생_횟수[i][0]]) > 1:
            answer.append(노래[총_재생_횟수[i][0]][0][1])
            answer.append(노래[총_재생_횟수[i][0]][1][1])

    return answer

# [4, 1, 3, 0]
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
# [5, 1, 4, 7, 3, 0, 6]
print(solution(["classic", "pop", "classic", "classic","jazz","pop", "Rock", "jazz"], [500, 600, 150, 800, 1100, 2500, 100, 1000]))
# [0, 1, 2, 4]
print(solution(["A", "A", "B", "A", "B", "B", "A", "A", "A", "A"],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
# [1, 0]
print(solution(['B', 'A'], [500, 600]))
