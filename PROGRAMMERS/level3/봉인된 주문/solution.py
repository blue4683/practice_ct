def solution(n, bans):
    answer = ''
    bans.sort()
    for ban in bans:
        tmp = 0
        k = 1
        for i in range(len(ban)):
            tmp += k
            k *= 26

        k = 1
        for i in range(len(ban) - 1, -1, -1):
            tmp += k * (ord(ban[i]) - ord('a'))
            k *= 26

        if tmp <= n:
            n += 1

    l = 0
    k = 1
    while k < n:
        n -= k
        k *= 26
        l += 1

    k //= 26
    for i in range(l):
        answer += chr(ord('a') + n // k)
        n %= k
        k //= 26

    return answer
