def solution(distance, rocks, n):
    answer = -1

    rocks.sort()

    left = 1
    right = distance
    rocks.append(distance)

    while left <= right:
        mid = (left + right) // 2

        delete = 0
        pre_rock = 0 # 이전 바위의 위치
        for rock in rocks:
            dist = rock - pre_rock
            if dist < mid:
                delete += 1

                if delete > n:
                    break
            else:
                pre_rock = rock

        if delete > n:
            right = mid - 1
        else:
            answer = max(answer, mid)
            left = mid + 1

    return answer

# 0 2 11 14 17 21 25
#  2 9  3  3  4  4
# (sort 후) 2 3 3 4 4 9
# 2개 제거 하면 -> 바위 사이의 거리 리스트에서도 2개가 제거된다
# 2 9 3 11 - [17, 21] 제거
# 11 3 3 8 - [2, 21] 제거
# 4
print(solution(25, [2, 14, 11, 21, 17], 2))