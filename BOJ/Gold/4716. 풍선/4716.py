import sys
input = sys.stdin.readline

while 1:
    n, a, b = map(int, input().split())
    if (n, a, b) == (0, 0, 0):
        break

    teams = [list(map(int, input().split())) for _ in range(n)]
    teams.sort(key=lambda x: -abs(x[1] - x[2]))

    result = 0
    for k, da, db in teams:
        if da <= db:
            if a >= k:
                result += da * k
                a -= k

            else:
                result += da * a + db * (k - a)
                b -= (k - a)
                a = 0

        else:
            if b >= k:
                result += db * k
                b -= k

            else:
                result += db * b + da * (k - b)
                a -= (k - b)
                b = 0

    print(result)
