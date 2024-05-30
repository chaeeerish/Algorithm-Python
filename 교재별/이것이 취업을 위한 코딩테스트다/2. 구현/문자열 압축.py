def solution(s):
    length = []

    if len(s) == 1:
        return 1

    for n in range(1, len(s)):
        queue = []
        previous = 0
        current = 0
        queue.append((s[previous:previous + n], 1))

        rest = ''
        while True:
            current = previous + n

            if previous >= len(s):
                rest = s[current:]
                break

            if s[previous:previous + n] == s[current:current + n]:
                string, count = queue.pop()
                count += 1
                queue.append((string, count))
                previous = current
            else:
                queue.append((s[current:current + n], 1))
                previous = current

        result = ''
        for string, count in queue:
            if count == 1:
                result += string
            else:
                result += (str(count) + string)
        result += rest

        length.append(len(result))

    return min(length)

print(solution("a"))
