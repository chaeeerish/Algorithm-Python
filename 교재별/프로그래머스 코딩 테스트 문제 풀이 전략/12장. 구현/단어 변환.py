import copy

min_count = 51
words_len = 0


def is_one_letter_different(str1, str2):
    count = 0
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            count += 1

    if count == 1:
        return True
    else:
        return False


def dfs(begin, target, words):
    # print("words")
    # print(words)

    global min_count, words_len

    if len(words) == 0:
        return

    if begin == target:
        min_count = min(min_count, words_len - len(words))
        return

    for w in words:
        if is_one_letter_different(begin, w):
            print(w)
            words2 = copy.deepcopy(words)
            words2.remove(w)
            dfs(w, target, words2)


def solution(begin, target, words):
    global words_len
    words_len = len(words)

    dfs(begin, target, words)

    if min_count == 51:
        return 0
    return min_count