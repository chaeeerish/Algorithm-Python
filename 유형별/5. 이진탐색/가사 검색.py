def solution(words, queries):
    answer = []

    for query in queries:
        start, end = query.find('?'), query.rfind('?')
        keyword = query[:start] + query[end+1:]

        filtered = [word[:start] + word[end+1:] for word in words if len(word) == len(query) and word[:start] + word[end+1:] == keyword]
        answer.append(len(filtered))
    return answer

# [3, 2, 4, 1, 0]
print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))