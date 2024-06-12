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
    return answer```