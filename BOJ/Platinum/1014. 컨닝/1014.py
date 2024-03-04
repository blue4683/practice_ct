import sys
input = sys.stdin.readline


def check_seats(bit, y, width):
    for x in range(width):
        if bit & (1 << x) and seats[y][x] == 'x':
            return 0

    return 1


def is_possible(bit, width):
    for i in range(width - 1):
        val = 3 << i
        if bit & val == val:
            return 0

    return 1


def check_row(fbit, sbit, width):
    for i in range(width):
        if sbit & (1 << i):
            if i > 0 and (1 << (i - 1)) & fbit:
                return 0
            if (1 << (i + 1)) & fbit:
                return 0

    return 1


for _ in range(int(input())):
    n, m = map(int, input().split())
    seats = [input().rstrip() for _ in range(n)]
    dp = [[0] * (1 << m) for _ in range(n + 1)]

    bits = []
    for bit in range(1 << m):
        if is_possible(bit, m):
            cnt = 0
            for i in range(m):
                if bit & (1 << i):
                    cnt += 1
            bits.append((bit, cnt))

    result = 0

    for i in range(n):
        for fbit, fcnt in bits:
            if check_seats(fbit, i, m):
                for sbit, scnt in bits:
                    if check_row(fbit, sbit, m):
                        dp[i][fbit] = max(dp[i][fbit], dp[i - 1][sbit] + fcnt)
                        result = max(result, dp[i][fbit])

    print(result)
