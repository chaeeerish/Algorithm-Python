### 행렬 회전하기
- 90도 회전하기
```python
def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    
    for r in range(N):
      for c in range(N):
        ret[c][N - 1 - r] = m[r][c]
    return ret

print(rotate_90([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
```

- 참고 자료
  - https://shoark7.github.io/programming/algorithm/rotate-2d-array
  - https://yommi11.tistory.com/33

### 행렬의 곱셈
```python
def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]

    for row in range(len(arr1)):
        for col in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[row][col] += arr1[row][k] * arr2[k][col]
    return answer
```

zip과 sum을 사용하여 컴프리헨션으로 풀어낸 풀이는 다음과 같다.
```python
A = [[1, 4], [3, 2], [4, 1]]
B = [[3, 3], [3, 3]]
[[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
```

- 참고 자료
  - https://velog.io/@falling_star3/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level2-%ED%96%89%EB%A0%AC%EC%9D%98-%EA%B3%B1%EC%85%88
