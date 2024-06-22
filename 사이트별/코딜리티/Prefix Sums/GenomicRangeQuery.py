'''
DNA는 A, C, G, T로 구성된다. successive nucleotides에 상응하는
각 nucleotides는 impact factor를 가진다.
A, C, G, T
1, 2, 3, 4

특정 DNA의 특정 부분에 nucleotides의 최소 impact factor은 몇이야?
DNA = S = S[0]S[1]...S[N-1] (N개의 문자로 이루어진 문자열)

리스트 P와 Q의 M개의 쿼리가 있다.
K번째 쿼리는 P[K]와 Q[k] 사이의 DNA 배열을 포함하는 최소 impact factor을 찾도록 요청할 것이다.

'''


def solution(S, P, Q):
    result = []
    for i in range(len(P)):
        if 'A' in S[P[i]:Q[i] + 1]:
            result.append(1)
        elif 'C' in S[P[i]:Q[i] + 1]:
            result.append(2)
        elif 'G' in S[P[i]:Q[i] + 1]:
            result.append(3)
        else:
            result.append(4)
    return result


print(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))
