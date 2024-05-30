n, m, k = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

격자 = [[(-1, -1) for i in range(n)] for j in range(n)] # [[(), (), (), (), ()], [(), (), (), (), ()], [(), (), (), (), ()], [(), (), (), (), ()]]

현재_위치 = [() for _ in range(m)] # [(2, 0), (1, 1), (0, 4), (2, 4)]
for i in range(n):
    for j in range(n):
        if array[i][j] != 0:
            현재_위치[array[i][j] - 1] = (i, j)

현재_방향 = list(map(int, input().split())) # [4, 4, 3, 1]
for i in range(m):
    현재_방향[i] = 현재_방향[i] - 1

우선_순위 = [[] for _ in range(m)] # [[[2, 3, 1, 4], [4, 1, 2, 3], [3, 4, 2, 1], [4, 3, 1, 2]], [[2, 4, 3, 1], [2, 1, 3, 4], [3, 4, 1, 2], [4, 1, 2, 3]], [[4, 3, 2, 1], [1, 4, 3, 2], [1, 3, 2, 4], [3, 2, 1, 4]], [[3, 4, 1, 2], [3, 2, 4, 1], [1, 4, 2, 3], [1, 4, 2, 3]]]
for i in range(m):
    우선_순위[i].append(list(map(int, input().split()))) # 0 위
    우선_순위[i].append(list(map(int, input().split()))) # 1 아래
    우선_순위[i].append(list(map(int, input().split()))) # 2 왼쪽
    우선_순위[i].append(list(map(int, input().split()))) # 3 오른쪽

for i in range(m):
    for j in range(4):
        우선_순위[i][j] = [x - 1 for x in 우선_순위[i][j]]

def 우선순위_추출하기(상어_현재_방향, 상어_다음_방향, 상어_우선_순위):
    return 상어_우선_순위[상어_현재_방향].index(상어_다음_방향)

def 상어의_다음_위치(격자, 상어_현재_위치, 상어_현재_방향, 상어_우선_순위):
    후보 = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 아무 냄새 X
    for j in range(4):
        nx = 상어_현재_위치[0] + dx[j]
        ny = 상어_현재_위치[1] + dy[j]
        if 0 <= nx < len(격자) and 0 <= ny < len(격자) and 격자[nx][ny][0] == -1:
            후보.append((nx, ny, j))

    # 자신의 냄새
    if len(후보) == 0:
        for j in range(4):
            nx = 상어_현재_위치[0] + dx[j]
            ny = 상어_현재_위치[1] + dy[j]
            if 0 <= nx < len(격자) and 0 <= ny < len(격자) and 격자[nx][ny][0] == i:
                후보.append((nx, ny, j))

    # 방향 우선순위에 맞게 정렬
    if len(후보) == 1:
        return 후보[0]
    elif len(후보) == 0:
        for j in range(4):
            nx = 상어_현재_위치[0] + dx[j]
            ny = 상어_현재_위치[1] + dy[j]
            후보.append((nx, ny, j))
        후보.sort(key=lambda x: 우선순위_추출하기(상어_현재_방향, x[2], 상어_우선_순위))
    elif len(후보) >= 2:
        후보.sort(key=lambda x: 우선순위_추출하기(상어_현재_방향, x[2], 상어_우선_순위))

    return 후보[0]

상어_수 = m
시간 = 0
for _ in range(1001):
    # 종료 시점인지 검토
    if 상어_수 == 1:
        break
    else:
        시간 += 1

    for i in range(n):
        for j in range(n):
            if 격자[i][j][0] != -1:
                격자[i][j] = (격자[i][j][0], 격자[i][j][1] - 1)
                if 격자[i][j][1] == 0:
                    격자[i][j] = (-1, -1)

    # 자신의 위치에 냄새 뿌리기
    for i in range(m):
        if 현재_위치[i][0] != -1 and 현재_위치[i][1] != -1:
            격자[현재_위치[i][0]][현재_위치[i][1]] = (i, k)

    # 상,하,좌,우 이동
    for i in range(m):
        if 현재_위치[i][0] != -1 and 현재_위치[i][1] != -1:
            x, y, 방향 = 상어의_다음_위치(격자, 현재_위치[i], 현재_방향[i], 우선_순위[i])
            현재_위치[i] = (x, y)
            현재_방향[i] = 방향

    쫓겨날_후보 = dict()
    for i in range(m):
        if 현재_위치[i] != (-1, -1) and 현재_위치.count(현재_위치[i]) >= 2:
            # 여러 마리 상어라면, 가장 작은 번호를 가진 상어를 제외하고 모두 겪자 밖으로 쫓겨난다
            if 현재_위치[i] in 쫓겨날_후보.keys():
                쫓겨날_후보[현재_위치[i]].append(i)
            else:
                쫓겨날_후보[현재_위치[i]] = [i]

    for key in 쫓겨날_후보.keys():
        쫓겨날_후보[key].sort(reverse=True)
        for j in range(len(쫓겨날_후보[key]) - 1):
            현재_위치[쫓겨날_후보[key][j]] = (-1, -1)
            상어_수 -= 1

if 시간 == 1001:
    print(-1)
else:
    print(시간)

"""
# 14
5 4 4
0 0 0 0 3
0 2 0 0 0
1 0 0 0 4
0 0 0 0 0
0 0 0 0 0
4 4 3 1
2 3 1 4
4 1 2 3
3 4 2 1
4 3 1 2
2 4 3 1
2 1 3 4
3 4 1 2
4 1 2 3
4 3 2 1
1 4 3 2
1 3 2 4
3 2 1 4
3 4 1 2
3 2 4 1
1 4 2 3
1 4 2 3

# 9
4 5 6
0 0 0 0
0 3 0 0
2 0 1 0
0 4 0 5
3 4 2 1 3
4 1 3 2
4 2 3 1
1 2 4 3
2 3 1 4
1 3 2 4
4 1 3 2
4 3 2 1
1 4 3 2
2 3 1 4
4 3 2 1
1 4 3 2
4 2 3 1
4 3 2 1
1 4 3 2
1 3 2 4
3 2 1 4
2 3 1 4
3 2 4 1
2 3 4 1
1 2 4 3
"""