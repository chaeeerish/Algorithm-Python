### 가장 큰 수
🔗 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42746  
❗️ 배운점: 큰 수를 판가름하는 그 로직 .... x * 4를 생각해낼 수 있는 능력 할 수 있을까..  
```python
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: int((x*4)[0:4]), reverse=True)
    return str(int(''.join(numbers)))
```

### 입국심사
🔗 문제: https://school.programmers.co.kr/learn/courses/30/lessons/43238  
❗️ 배운점  
1. input의 길이가 지나치게 길다. 리스트의 길이가 100,000명 이하이며 하나의 input의 값이 1,000,000,000 이하이다.
2. **특정 값**(시간, 가격 ...)을 찾아야 한다.  

➡️ **혹시 `이진탐색`을 의심해보자**

3. 그리고, 시간 하나하나 셀 생각을 했지 이분 탐색이 가능한 생각을 전혀 못했다. 사람을 하나하나 더해갈 생각을 했지 시간에서 사람을 구할 생각을 못했다.

```python
def solution(n, times):
    left = 1
    right = max(times) * n

    while left <= right:
        mid = (left + right) // 2
        people = 0

        for time in times:
            people += mid // time

            if people >= n:
                break

        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer
```

### 징검다리
🔗 문제: https://school.programmers.co.kr/learn/courses/30/lessons/43236  
❗️ 배운점
1. left, right, mid를 이용한 이분 탐색의 대상을 문제에서 물어본 "징검다리 각 지점 사이의 거리의 최소값 중에 가장 큰 값"으로 잡았다.
2. 확실히 이분 탐색안에 전체 rock 반복문을 돌리니까 시간 복잡도가 확 줄어드는 것 같다.
```python
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
```

### 징검다리 건너기
🔗 문제: https://school.programmers.co.kr/learn/courses/30/lessons/64062  
❗️ 배운점: 간단하게 한다고 문자열 변환과 조인 연산을 수행하였는데 이게 오버 시간의 원인이 된 것 같다. 그래서 for문으로 바꾸고, 중간에 조건이 맞지 않으면 break하는 방식으로 변경하였다.
```python
        consecutive = 0
        for stone in stones:
            if stone <= mid:
                consecutive += 1
            else:
                consecutive = 0

            if consecutive >= k:
                break
```

### 베스트앨범
🔗 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42579  
❗️ 배운점: 딕셔너리의 정렬은 다음과 같다. `총_재생_횟수 = sorted(총_재생_횟수.items(), key=lambda item: item[1], reverse=True)`  
(.items()는 딕셔너리의 모든 키-쌍을 튜플로 반환한다.)

### MaxCounters
🔗 문제: https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/start/
1. 배운점: O(n)의 시간복잡도를 가지는 max 함수를 매번 호출할 필요가 뭐있어? 변수에 저장해두면 되지.
```python
def solution(N, A):
    result = [0] * N

    max_value = 0
    for i in range(len(A)):
        if A[i] == N + 1:
            result = [max_value] * N # [max(result)] * N
        else:
            result[A[i] - 1] += (1 + max_value)
            if result[A[i] - 1] > max_value:
                max_value = result[A[i] - 1]

    return result
```
2. 배운점: 최대한 변수에 저장해서, O(n^2)를 만들지 말자.
```python
def solution(N, A):
    result = [0] * N

    max_value = 0
    last_update = 0
    for i in range(len(A)):
        if 1 <= A[i] <= N:
            if result[A[i] - 1] < last_update:
                result[A[i] - 1] = last_update
            result[A[i] - 1] += 1
            if result[A[i] - 1] > max_value:
                max_value = result[A[i] - 1]
        else:
            last_update = max_value

    for i in range(len(result)):
        if result[i] < last_update:
            result[i] = last_update

    return result
```

### Triangle
🔗 문제: https://app.codility.com/c/run/trainingX4FUTA-4TC/
❗️ 배운점: 100000개의 배열에서 3개 조합을 찾는 것은 n^3의 시간복잡도에 가까운 일이므로 불가능하다.  
또한, 다음의 조건을 만족하기 위해서는 인접한 인덱스만 비교하면 된다. 따라서, O(n)의 시간복잡도로 풀 수 있다.
- A[P] + A[Q] > A[R],
- A[Q] + A[R] > A[P],
- A[R] + A[P] > A[Q].

### NumberOfDiscIntersections
🔗 문제: https://app.codility.com/programmers/lessons/6-sorting/number_of_disc_intersections/start/
❗️ 배운점: 문제를 푸는 방식을 아예 생각을 못했다. 정렬을 하다니 .. 그리고 겹치는 부분을 1씩 늘려가다니 ..
![img.png](img.png)  
(출처: https://lipcoder.tistory.com/197)

```python
def solution(A):
    events = []
    for i, v in enumerate(A):
        events.append(((i - v), -1))
        events.append(((i + v), 1))
    events.sort()

    result = 0
    count = 0

    for i in range(len(events)):
        if events[i][1] == 1:
            count -= 1
        elif events[i][1] == -1:
            result += count
            count += 1

        if result > 10000000:
            return -1
    return result
```

### NumberOfDiscIntersections
🔗 문제: https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/   
❗️ 배운점: 상류로 올라가는 물고기가 한 물고기를 먹고 그 뒤에 있는 물고기도 먹을 수 있다는걸 고려하지 못했다.. !!! 틀린 이유는 꼼꼼히 적으면서 문제를 보지 않아서 그런듯 하다.
```python
def solution(A, B):
    queue = deque()

    for i in range(0, len(A)):
        if B[i] == 1:
            queue.append((B[i], A[i]))
        else: # B[i] == 0:
            queue.append((B[i], A[i]))
            j = len(queue) - 1
            while 0 <= j <= len(A) - 1:
                if queue[j - 1][0] == 1:
                    elem_j = queue.pop()
                    elem_j_1 = queue.pop()
                    if elem_j[1] > elem_j_1[1]:
                        queue.append(elem_j)
                        j -= 1
                    else:
                        queue.append(elem_j_1)
                        break
                else: # queue[j - 1][0] == 0:
                    break

    return len(queue)
```

### StoneWall
🔗 문제: https://app.codility.com/programmers/lessons/7-stacks_and_queues/stone_wall/  
❗️ 배운점: all을 사용하면 O(n^2)이 될 수 있다. 문제를 푸는 방식을 아예 생각을 못했다. 사실 시간복잡도를 많이 줄였음에도 타임에러가 발생했다. 그럴만 하다. 다음 해설 코드에서는 리스트를 한번만 읽고 답을 내기 때문이다.  
많이 예시를 그려보고 원리를 찾으면 될까?  

**이 문제에서 사용한 방식은 다음과 같다. 스택을 이용하고 이전의 블럭보다 큰 블럭을 세우고자 하면 blockCount를 올린다.**

```python
def solution(H):
    blockCount = 0
    blockStack = []

    for i in range(len(H)):
        while blockStack and blockStack[-1] < H[i]:
            blockStack.pop()

        if not blockStack or blockStack[-1] > H[i]:
            blockCount += 1
            blockStack.append(H[i])

    return blockCount
```

### EquiLeader
🔗 문제: https://app.codility.com/programmers/lessons/8-leader/equi_leader/  
❗️ 배운점
1. 전체의 Leader 이어야만 나눴을 때도 Leader가 될 수 있는줄 몰랐다... 여러 예시로 시뮬레이션을 해보지 않아서 생긴 결과가 아닐까... Codility는 테스트 케이스가 불친절해서 더 그런 것 같다!!!
2. **특정 count를 세기 위해서 이중 for문을 할 필요가 없다. left_count를 하나씩 늘려가면 ➡️ O(n) 시간으로 모든 count를 셀 수 있다.** (**🚨 이 문제의 핵심 🚨**)

```python
for i in range(len(A) - 1):
    left_count = sum(1 for x in value_index if x <= i)
    right_count = len(value_index) - left_count
```
⬇️
```python
for i in range(len(A) - 1):
    if A[i] == value:
        left_count += 1
        right_count = full_count - left_count
```

### MaxProfit
🔗 문제: https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_profit/  
❗️ 배운점:  
1. 그냥 지금 값에서 최소값을 빼면 된다.
2. 따라서, 최소 값은 그때마다 O(n)을 사용할 필요가 없다.
3. **어차피, for문을 돌면서 모든 값을 거칠 것이니 최소값을 갱신하면 된다.**

![img_1.png](img_1.png)
```python
    for i in range(1, len(A)):
        min_value = min(min_value, A[i])
        result = max(result, A[i] - min_value)
```

### MaxSlice
🔗 문제: https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_slice_sum/  
❗️ 배운점: 최대 부분합을 구하는 알고리즘 외우자 ... 
![img_1.png](img_1.png)

### MaxDoubleSliceSum
🔗 문제: https://app.codility.com/programmers/lessons/9-maximum_slice_problem/max_double_slice_sum/  
❗️ 배운점: 알고리즘 해결 방법 ... 왼쪽 합과 오른쪽 합을 이용해서 O(n)의 시간 복잡도로 끝냈다. 알아두면 무조건 좋을 해결 방법인 것 같다.
```python
def solution(A):
    left_sum = [0] * len(A)
    right_sum = [0] * len(A)

    for i in range(1, len(A)):
        left_sum[i] = max(0, left_sum[i-1] + A[i])

    for i in range(len(A) - 2, -1, -1):
        right_sum[i] = max(0, right_sum[i + 1] + A[i])

    result = 0
    for i in range(1, len(A) - 1):
        result = max(result, left_sum[i - 1] + right_sum[i + 1])
    return result
```

### 정수 삼각형
🔗 문제: https://school.programmers.co.kr/learn/courses/30/lessons/43105#  
❗️ 배운점: 기록할 수 있는건 무조건 기록해두자. 그게 시간을 줄이는 가장 좋은 방법이다. `DP => Dynamic Programming`

### 등굣길
🔗 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42898#  
❗️ 배운점  
1️⃣ 문제를 완전 잘못 이해 => 최단 경로인줄 알았는데 최단 경로의 개수 였음 ...  
2️⃣ 뭐에 홀렸는지 최단경로 계산하는 방법을 완전히 다르게 했다 ...  
3️⃣ 다음과 같은 방법은 최단 경로가 아니라 출발지에서 목적지까지 도착할 수 있는 경로의 개수를 나타내는 식이다.  
![img_2.png](img_2.png)  
(출처: https://dev-note-97.tistory.com/141)

### 가장 먼 노드
🔗 문제: https://school.programmers.co.kr/learn/courses/30/lessons/49189  
❗️ 배운점: BFS와 그래프가 익숙하지 않아서 그런 것 같다. 여러번 풀어봐야지 그래프!!! => **특정 점에서 각 노드로의 거리를 알고 싶다면 `BFS/QUEUE/연결리스트`**  

### 2개 이하로 다른 비트
🔗 문제: https://school.programmers.co.kr/learn/courses/30/lessons/77885  
❗️ 배운점  
1️⃣ 2개의 비트를 변경할 때, 인접한 비트만 변경하면 된다. 그래야 최소를 찾을 수 있다. => 따라서, 이중 for문을 돌릴 필요가 없었다.  
2️⃣ 1개의 비트를 변경할 때, 0번째 자리부터 비교하여 후보를 찾으면 바로 for문을 나가도 된다. => 이 수보다 작은 수 찾을 수 없음
```python
        for a in range(49, -1, -1):
                b = a - 1
                new_bin = int('0b' + bin_number[:b] + str(int(bin_number[b]) ^ 1) + bin_number[b + 1:a] + str(int(bin_number[a]) ^ 1) + bin_number[a + 1:], 2)
                if new_bin > cand:
                    break
                if new_bin < cand and new_bin > number:
                    cand = new_bin
```

### 순위
🔗 문제: https://school.programmers.co.kr/learn/courses/30/lessons/49191#  
❗️ 배운점   
1️⃣ 먼저, board라는 2차원 배열에 각 간선에 대한 정보를 업데이트하고 앞으로는 board만 사용한다.  
```python
    for a, b in results:
        board[a - 1][b - 1] = 1
        board[b - 1][a - 1] = -1
```
2️⃣ 플로이드-와샬 알고리즘을 적용하여 중간 경유점을 통해 i와 j의 승패 관계를 도출한다.  
```python
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or board[i][j] in [1, -1]:
                    continue
                if board[i][k] == board[k][j] == 1:
                    board[i][j] = 1

                if board[i][k] == board[k][j] == -1:
                    board[i][j] = -1
```
3️⃣ 승패 관계가 n-1개 정해진 선수에 대해서 모든 승패가 결정되었다고 판단한다.  

### 길 찾기 게임
🔗 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42892  
❗️ 배운점  
1️⃣ `런타임 에러`에서 재귀 깊이를 늘렸더니 해결되었다. 
```python
import sys
sys.setrecursionlimit(10**6)
```
2️⃣ **트리를 클래스로 만들었다.**
```python
class Node:
    def __init__(self, item, x, y):
        self.item = item
        self.x = x
        self.y = y
        self.left = None
        self.right = None

    def get_left_item(self):
        if self.left is None:
            return 0
        else:
            return self.left.item

    def get_right_item(self):
        if self.right is None:
            return 0
        else:
            return self.right.item

class BinaryTree:
    def __init__(self, root):
        self.root = root
```

### 디스크 컨트롤러
🔗 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42627  
❗️ 배운점: 문제를 해결하는 방식조차 생각하지 못했다. 다시 무조건 풀어봐야겠다.  
```python
# 파이썬 최소힙
import heapq

heap = []
heapq.heappush(heap, 50)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)

print(heap)
```

### 보석 쇼핑
🔗 문제: https://school.programmers.co.kr/learn/courses/30/lessons/67258  
❗️ 배운점  
**효율성 통과를 위한 노력**  
1️⃣ 이중 for문 절대 안됨 X
2️⃣ itertools 절대 안됨 X  
3️⃣ 슬라이딩 윈도우 방식 (start와 end 포인터를 이용해서 윈도우를 확장시키거나 축소시킨다.)  
4️⃣ while문 내에서 리스트 인덱스 절대 안됨 X (`if set(gems[start:end+1]) == type:`)  
5️⃣ 리스트, 집합은 O(1), O(N)의 시간복잡도를 가지므로 `Dict` 자료구조를 사용하였다.  
6️⃣ 그럼에도 불구하고, Dict.keys()에서 효율성이 초과되었다. => 따라서, valdiate_count를 이용하여 변수에 보석의 개수를 관리하였다.  

### 비밀번호
🔗 문제: https://www.acmicpc.net/problem/1816
❗️ 배운점: 100000 이하에 소인수가 있는지 확인만 하면 되는데 왜 수의 끝까지 갔는지 모르겠다... 바보 같았다...
```python
answer = []
for i in range(n):
    flag = True
    for j in range(2, 1000000):
        if array[i] % j == 0:
                flag = False
                break
```

### 모이기
🔗 문제: [2주만에 통과하는 알고리즘 코딩테스트] 1-(5)  
❗️ 배운점  
1️⃣ X 좌표, Y 좌표 따로 생각할 수 있다.
2️⃣ 각각의 학생들의 집에서 만나는게 가장 효율적이다.

### 조명
🔗 문제: [2주만에 통과하는 알고리즘 코딩테스트] 2-(1)  
❗️ 배운점  
```text
배수마다 깃발을 뒤집는 구조이다.

나의 생각)
1의 배수 => 1, 2, 3, 4, ...
2의 배수 => 2, 4, 6, 8, ...

수학적 생각)
1은 약수가 1개이므로, 한 번 뒤집힌다. (백)
2는 약수가 2개이므로, 두 번 뒤집힌다. (청)
3은 약수가 2개이므로, 두 번 뒤집힌다. (청)
4는 약수가 3개이므로, 세 번 뒤집힌다. (백)
5는 약수가 2개이므로, 두 번 뒤집힌다. (청)
6은 약수가 4개이므로, 네 번 뒤집힌다. (청)
...
9는 약수가 3개이므로, 세 번 뒤집힌다. (백)

=> 규칙: 루트 N이 정수일 때, 약수가 홀수이다. 즉, 백기이다.
```