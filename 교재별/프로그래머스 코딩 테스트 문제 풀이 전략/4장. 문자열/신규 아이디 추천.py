def solution(new_id):
    # 1
    new_id = new_id.lower()

    # 2
    cnt = 0
    while True:
        if not (new_id[cnt].isalnum() or new_id[cnt] == '-' or new_id[cnt] == '_' or new_id[cnt] == '.'):
            new_id = new_id.replace(new_id[cnt], '')
            cnt = cnt
        else:
            cnt += 1
        if cnt >= len(new_id):
            break

    # 3
    while True:
        if '..' not in new_id:
            break
        new_id = new_id.replace('..', '.')

    # 4
    if len(new_id) >= 1 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) >= 1 and new_id[-1] == '.':
        new_id = new_id[:-1]

    # 5
    if len(new_id) == 0:
        new_id = 'a'

    # 6
    if len(new_id) >= 15:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    # 7
    while True:
        if len(new_id) <= 2:
            new_id += new_id[-1]
        else:
            break

    return new_id

# "bat.y.abcdefghi"
print(solution("...!@BaT#*..y.abcdefghijklm"))
# "z--"
print(solution("z-+.^."))
# "aaa"
print(solution("=.="))
# "123_.def"
print(solution("123_.def"))
# "abcdefghijklmn"
print(solution("abcdefghijklmn.p"))
