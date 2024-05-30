## 이진 탐색 - 범위를 반씩 좁혀가는 탐색
이진 탐색이란 리스트 내에서 데이터를 매우 빠르게 탐색하는 알고리즘이다.

### 순차 탐색
- 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인한다.
```python
def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1
```
- 시간 복잡도
  - 데이터의 정렬 여부와 상관없이 데이터의 개수가 N개 일때 N번의 비교 연산이 필요하다.
  - O(N)

### 이진 탐색
- "반으로 쪼개면서 탐색하기"
- 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘이다.
- 이진 탐색은 변수 3개를 사용한다.
  - 시작점
  - 끝점
  - 중간점
- 재귀함수로 구현한 이진 탐색 소스코드
```python
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid + 1, end)
```
- 반복문으로 구현한 이진 탐색 소스코드
```python
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None
```
- 시간 복잡도
  - 한 번 확인할 때마다 확인하는 원소의 개수가 절반씩 줄어든다는 점에서 시간 복잡도가 O(logN)이다.
  - 탐색 범위가 2000만을 넘어가면 이진 탐색으로 문제에 접근해보자.

### 트리 자료구조
- 노드와 노드의 연결로 표현되어 있다.
- 많은 양의 데이터를 관리하기 위한 목적으로 사용한다.
- 이진 탐색 트리
  - 이진 탐색이 동작할 수 있도록 고안된, 효율적인 탐색이 가능한 자료구조이다.
  - `왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드`가 성립해야지 이진 탐색 트리이다.
- 이진 탐색 문제는 입력 데이터가 많거나 탐색의 범위가 매우 넓다.
  - 데이터의 개수가 1000만 개를 넘어가거나 탐색 범위의 크기가 1000억 이상이라면 이진 탐색 알고리즘을 의심할 수 있다.
  - 이렇게 입력 데이터의 개수가 많은 문제에는 input() 함수를 사용하면 시간 초과가 날 수 있다.
  - sys 라이브러리의 readline() 함수를 이용하여 시간 초과를 피할 수 있다.
```python
import sys

sys.stdin.readline().rstrip()
```

### 문제 - 부품 찾기
- 문제 설명
  - 부품이 N개 있다.
  - M개 종류의 부품이 있는지를 확인한다.
- 문제 해설
  - 세 가지 방식으로 풀 수 있다.
    - 이진 탐색 알고리즘
    - 계수 정렬
    - 집합 자료형 이용

### 문제 - 떡볶이 떡 만들기
- 문제 설명
  - 손님이 요쳥한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최대값
  - 입력
    - 떡의 개수 N, 요청한 떡의 길이 M
    - 떡의 개별 높이
  - 출력
    - 절단기 높이의 최대값
- 문제 해설
  - 파라메트릭 서치
    - 최적화 문제를 결정 문제로 바꾸어 해결하는 기법이다.
    - 이진 탐색을 이용하여 해결할 수 있다.
    - 원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제에 주로 파라메트릭 서치를 사용한다.