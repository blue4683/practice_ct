import sys
input = sys.stdin.readline

n, m = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
garbages = [(y, x) for y in range(n) for x in range(m) if room[y][x]]

result = 0
while 1:
    result += 1
    new = []
    sy, sx = 0, 0
    for y, x in garbages:
        if y >= sy and x >= sx:
            sy, sx = y, x

        else:
            new.append((y, x))

    if not new:
        break

    garbages = new[:]

print(result)
