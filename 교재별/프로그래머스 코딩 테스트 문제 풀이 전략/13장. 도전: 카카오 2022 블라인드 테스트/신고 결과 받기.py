def solution(id_list, report, k):
    answer = []

    reporting = dict()
    for id in id_list:
        reporting[id] = list()

    reported = dict()
    for id in id_list:
        reported[id] = 0

    for r in report:
        이용자, 신고자 = r.split()
        if 신고자 not in reporting[이용자]:
            reporting[이용자].append(신고자)
            reported[신고자] += 1

    #     print(reporting)
    #     print(reported)

    for id in id_list:
        cnt = 0
        for 신고자 in reporting[id]:
            if reported[신고자] >= k:
                cnt += 1
        answer.append(cnt)

    return answer