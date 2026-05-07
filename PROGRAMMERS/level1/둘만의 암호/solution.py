def solution(s, skip, index):
    answer = ''
    skip = set(skip)
    mod = ord('a')
    for alp in s:
        i = index
        while i:
            alp = chr(mod + ((ord(alp) - mod + 1) % 26))
            if alp not in skip:
                i -= 1

        answer += alp

    return answer
