def solution(beginning, target):
    answer = 10 ** 9
    n, m = len(beginning), len(beginning[0])

    def flip(fy, fx):
        for y in range(n):
            for x in range(m):
                f = beginning[y][x] ^ (((fy >> y) & 1) ^ ((fx >> x) & 1))
                if f != target[y][x]:
                    return -1

        return list(bin(fy)).count('1') + list(bin(fx)).count('1')

    for fy in range(1 << n):
        for fx in range(1 << m):
            cnt = flip(fy, fx)
            if cnt >= 0:
                answer = min(answer, cnt)

    return answer if answer != 10 ** 9 else -1
