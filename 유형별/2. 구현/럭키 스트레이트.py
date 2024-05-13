# 특정 조건
# 점수 N을 자릿수 기준으로 점수 N을 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황

n = input()
array = list(map(int, n))
mid = int(len(array)/2)

array1 = array[0:mid]
array2 = array[mid:]

if sum(array1) == sum(array2):
    print("LUCKY")
else:
    print("READY")
