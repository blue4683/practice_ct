def solution(s):
    answer = 0
    target = ''
    index, a, b = 0, 0, 0
    n = len(s)
    while index < n:
        if target == '':
            target = s[index]

        if target == s[index]:
            a += 1

        else:
            b += 1

        if a == b:
            answer += 1
            target, a, b = '', 0, 0

        index += 1

    if a or b:
        answer += 1

    return answer
