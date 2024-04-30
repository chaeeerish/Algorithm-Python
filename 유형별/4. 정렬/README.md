## 정렬
### 기준에 따라 데이터를 정렬
- 정렬은 데이터를 특정한 기준에 따라서 순서대로 나열하는 것이다.
- 정렬 알고리즘으로 데이터를 정렬하면 이진 탐색이 가능해진다.
- 종류
  - 선택 정렬
  - 삽입 정렬
  - 퀵 정렬
  - 계수 정렬
- 또한, 파이썬에서 특정한 리스트의 원소를 뒤집는 메서드를 제공한다. 따라서, 내림차순 정렬은 오름차순 정렬을 수행한 뒤에 그 결과를 뒤집기하여 만들 수 있다.

### 선택 정렬
- **처리되지 않는 데이터 중에서 가장 작은 것과 바꾸기**
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]

print(array)
```
- 시간 복잡도
  - O(N^2)

### 삽입 정렬
- **데이터를 하나씩 확인하며 어떤 위치에 삽입하면 좋을지**
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
      if array[j] < array[j-1]:
        array[j], array[j-1] = array[j-1], array[j]
      else:
        break

print(array)
```
- 시간 복잡도
  - O(N^2)

### 퀵 정렬
- **기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다.**
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
      while left <= end and array[left] <= array[pivot]:
        left += 1
      while right > start and array[right] >= array[pivot]:
        right += 1
      if left > right:
        array[right], array[pivot] = array[pivot], array[right]
      else:
        array[right], array[left] = array[left], array[right]
        
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
```
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
```
- 시간 복잡도
  - O(NlogN)

### 계수 정렬
- 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르다.
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end = ' ')
```
- 시간 복잡도
  - O(N + K)

### 파이썬의 정렬 라이브러리
- 현대의 정렬 알고리즘은 정립되어 있기 때문에 앞으로는 큰 개선이 이루어질 것으로 예상하기는 어렵다.
- 따라서, 정렬 알고리즘 문제는 어느 정도 정해진 답이 있는, 즉 외워서 잘 풀어낼 수 있는 문제라고 할 수 있다.
- 기본 정렬 라이브러리인 sorted() 함수를 제공한다.
- 시간 복잡도
  - O(NlogN)
  - 정렬 라이브러리는 항상 최악의 경우에도 시간 복잡도 O(NlogN)을 보장한다.
- 문제에서 별도의 요구가 없다면 단순히 정렬해야 하는 상황에서는 기본 정렬 라이브러리를 사용하고, 데이터의 범위가 한정되어 있으며 더 빠르게 동작해야 할 때는 계수 정렬을 사용하자.
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
result = sorted(array)
print(result)
```

```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
array.sort()
print(array)
```

```python
array = [('바나나', 2), ('사과', 5), ('사과', 3)]
def setting(data):
    return data[1]
result = sorted(array, key=setting)
print(result)
```

- 문제 유형
  - 정렬 라이브러리로 풀 수 있는 문제
    - 단순히 정렬 기법을 알고 있는지 물어보는 문제로 기본 정렬 라이브러리의 사용 방법을 숙지하고 있으면 어렵지 않게 풀 수 있다.
  - 정렬 알고리즘의 원리에 대해서 물어보는 문제
    - 선택 정렬, 삽입 정렬, 퀵 정렬 등의 원리를 알고 있어야 문제를 풀 수 있다.
  - 더 빠른 정렬이 필요한 문제
    - 퀵 정렬 기반의 기법으로는 풀 수 없으며 계수 정렬 등의 다른 정렬 알고리즘을 이용하거나 기존에 알려진 알고리즘의 구조적인 개선을 거쳐야 풀 수 있다.

### 문제 - 위에서 아래로
- 문제 분석
  - 내림차순으로 정렬하는 프로그램
- 