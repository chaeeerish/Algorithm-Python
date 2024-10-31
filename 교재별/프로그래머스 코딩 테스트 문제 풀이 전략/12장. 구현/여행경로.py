import copy

answer = []


def dfs(dictionary1, start, tickets, temp):
    global answer

    if len(tickets) + 1 == len(temp):
        answer.append(temp)
        return

    if start not in dictionary1.keys() or len(dictionary1[start]) == 0:
        return

    # start가 다음으로 갈 수 있음
    for end in dictionary1[start]:
        dictionary2 = copy.deepcopy(dictionary1)
        dictionary2[start].remove(end)

        dfs(dictionary2, end, tickets, temp + [end])


def solution(tickets):
    global answer

    dictionary = dict()
    for t in tickets:
        if t[0] in dictionary.keys():
            dictionary[t[0]].append(t[1])
        else:
            dictionary[t[0]] = [t[1]]

    for key in dictionary.keys():
        dictionary[key].sort()

    dfs(dictionary, 'ICN', tickets, ['ICN'])

    return answer[0]