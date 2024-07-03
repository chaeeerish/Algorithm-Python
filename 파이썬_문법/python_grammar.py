# 수
a = 1000
a = -7
a = 0

a = 157.93
a = -182.775
a = 5.
a = .7

# 10의 9제곱 = 1*10^9
# 무한을 의미하기도 한다
a = 1e9
a = 75.25e1 # 752.5
a = 3594e-3 # 3.954

round(123.456, 2) # 123.46

7 / 3 # 2.3333333333333~
7 % 3 # 1
7 // 3 #2
5 ** 3 # 125

# 리스트 (내부적으로 연결 리스트 자료구조로 구현되어 있다.)
l = [1, 2, 3, 4, 5, 6]
print(l[1]) # 2
print(l[-1]) # 6
print(l[1:4]) # [2, 3, 4, 5]

l = list() # 빈 리스트
l = [] # 빈 리스트

array = [i for i in range(20) if i % 2 == 1] # 리스트 컴프리헨션 (2차원 리스트를 초기화할 때 리스트 컴프리헨션을 이용해야 한다.)
array = [[0] * 4 for _ in range(3)] # 언더바: 반복을 수행하되 반복을 위한 변수 무시

# 리스트 관련 메소드
array = [1, 4, 3]
array.append(2)
array.sort()
array.sort(reverse=True)
array.reverse()
array.insert(2, 3) # 시간 복잡도 O(N)
array.remove(1) # 시간 복잡도 O(N)

# 문자열
data = ""
data = ''

s1 = "Hello"
s2 = "World"
s1 + " " + s2

s1*3

s1[2:4]

# 튜플
#  - 선언된 값을 변경할 수 없다.
#  - 리스트에 비해서 상대적으로 공간 효율적이다.
#  - 각 원소의 성질이 다를 때 주로 사용한다.
a = (1, 2, 3, 4)
a[2]

# 사전
# (기본적으로 검색 및 수정에 있어서 O(1)의 시간에 처리할 수 있다.)
data = dict()
dict['사과'] = 'Apple'
dict['바나나'] = 'Banana'
dict['코코넛'] = 'Coconut'

if '사과' in data:
    print("\'사과\'를 키로 가지는 데이터가 존재합니다.")

key_list = data.keys()
value_list = data.values()

# 집합
# (순서가 없기 때문에 인덱싱으로 값을 얻을 수 없다.)
a = set([1, 1, 2, 2, 3, 4, 5]) # [1, 2, 3, 4, 5] 중복이 제거된다.
b = set([3, 4, 5, 6, 7])

a | b # 합집합
a & b # 교집합
a - b # 차집합

a.add(10)
a.update([11, 12])
a.remove(3)

# 기타 연산자
score = 85
result = "Success" if score >= 80 else "Fail"

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
result = [i for i in a if i not in remove_set]

# 함수
def func():
    global array # 함수 밖의 변수 데이터를 사용하기 위한 global 키워드
    array = [1, 2, 3, 4]
    array.append(5)

# 람다
print((lambda a, b: a + b)(3, 7))
print(sorted(a, key=lambda x: x[1]))

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
result = map(lambda a, b: a + b, list1, list2)
print(list(result))

# 입출력
n = int(input())
data = list(map(int, input().split()))
n, m, k = map(int, input().split())

import sys
data = sys.stdin.readline().rstrip()

answer = 7
print("정답은 " + str(answer) + "입니다.")
print("정답은 ", str(answer), "입니다.")
print(f"정답은 {answer}입니다.")