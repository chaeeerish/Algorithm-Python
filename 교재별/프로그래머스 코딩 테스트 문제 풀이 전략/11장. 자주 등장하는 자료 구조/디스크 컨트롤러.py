import heapq


def solution(jobs):
    answer, start, end, finish = 0, -1, 0, 0
    heap = []
    sum = 0

    while finish < len(jobs):
        for job in jobs:
            if start < job[0] <= end:
                heapq.heappush(heap, [job[1], job[0]])

        if len(heap) > 0:
            now_job = heapq.heappop(heap)
            start = end
            end += now_job[0]
            sum += (end - now_job[1])
            finish += 1
        else:
            end += 1

    return round(sum / len(jobs))

print(solution([[0, 3], [1, 9], [2, 6]])) # 9
print(solution([[7, 8], [3, 5], [9, 6]])) # 9