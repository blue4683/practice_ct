def solution(targets):
    answer = 1
    targets.sort()
    s, e = targets[0]
    n = len(targets)
    for i in range(1, n):
        a, b = targets[i]
        if a >= e:
            s, e = a, b
            answer += 1
            continue

        if a < e:
            s = a

        if b < e:
            e = b

    return answer
