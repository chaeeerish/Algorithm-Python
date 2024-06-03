def 맨해튼_거리_구하기(응시자1, 응시자2):
    return abs(응시자1[0] - 응시자2[0]) + abs(응시자1[1] - 응시자2[1])

def 파티션으로_막혀있는가(대기실, 응시자1, 응시자2):
    row1, col1 = min(응시자1[0], 응시자2[0]), min(응시자1[1], 응시자2[1])
    row2, col2 = max(응시자1[0], 응시자2[0]), max(응시자1[1], 응시자2[1])

    for row in range(row1, row2 + 1):
        for col in range(col1, col2 + 1):
            if 대기실[row][col] == 'O':
                return False
    return True

def solution(places):
    answer = []

    for 대기실 in places:
        응시자_리스트 = []
        for row in range(len(대기실)):
            for col in range(len(대기실[0])):
                if 대기실[row][col] == 'P':
                    응시자_리스트.append((row, col))

        flag = True
        for i in range(len(응시자_리스트)):
            for j in range(i + 1, len(응시자_리스트)):
                맨해튼_거리 = 맨해튼_거리_구하기(응시자_리스트[i], 응시자_리스트[j])
                if 맨해튼_거리 <= 1 or (맨해튼_거리 == 2 and 파티션으로_막혀있는가(대기실, 응시자_리스트[i], 응시자_리스트[j]) == False):
                    flag = False
                    break

            if flag == False:
                break

        if flag == False:
            answer.append(0)
        else:
            answer.append(1)

    return answer

# [1, 0, 1, 1, 1]
print(solution([["PPPPP", "XXXXX", "XXXXX", "XXXXX", "XXXXX"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))