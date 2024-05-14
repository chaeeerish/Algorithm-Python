"""
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D
"""

"""
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L
"""

"""
10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L
"""

# current direction
# 0      1    2    3
# N 북, E 동, S 남, W 서

def switch_direction(current_direction, turn):
    if turn == 'D':
        current_direction += 1
        if current_direction >= 4:
            current_direction = 0
    else:
        current_direction -= 1
        if current_direction < 0:
            current_direction = 3

    return current_direction

def go_straight(head, current_direction):
    if current_direction == 0:
        return head[0] - 1, head[1]
    elif current_direction == 1:
        return head[0], head[1] + 1
    elif current_direction == 2:
        return head[0] + 1, head[1]
    else: # current_direction == 3:
        return head[0], head[1] - 1

n = int(input()) # 보드의 크기
k = int(input()) # 사과의 개수

apple = []
for _ in range(k):
    i, j = map(int, input().split())
    apple.append((i - 1, j - 1))

l = int(input()) # 뱀 방향 변환 횟수
direction = dict()
for _ in range(l):
    x, c = map(str, input().split())
    x = int(x)

    direction[x] = c

snake = [(0, 0)] # 꼬리[0] ... 머리[-1]
time = 0
turn = 'D'
current_direction = 1

while True:
    # 방향 전환이 있나요?
    if time in direction.keys():
        current_direction = switch_direction(current_direction, direction[time])

    # 1. 앞으로 이동
    next_head = go_straight(snake[-1], current_direction)

    time += 1

    # 종료 규칙
    # a. 벽에 부딪혔나요?
    if next_head[0] >= n or next_head[0] < 0 or next_head[1] >= n or next_head[1] < 0:
        break
    # b. 몸에 부딪혔나요?
    if next_head in snake:
        break

    # 2. 사과가 있나요
    if next_head in apple:
        snake.append(next_head)
    # 3. 사과가 없나요
    else:
        snake.append(next_head)
        del snake[0]

print(time)