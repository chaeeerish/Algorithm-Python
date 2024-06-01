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