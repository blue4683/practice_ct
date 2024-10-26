import sys
input = sys.stdin.readline

n = int(input())
rooms = [int(input()) for _ in range(n)]
dist = [0] * n

while 1:
    blank = 0
    for i in range(n - 1, -1, -1):
        if not rooms[i]:
            blank = i
            break

    else:
        break

    exist = blank
    d = 0
    for i in range(exist - 1, -1, -1):
        if rooms[i]:
            d = exist - i
            exist = i
            break

    else:
        for i in range(n - 1, exist, -1):
            if rooms[i]:
                d = exist + n - i
                exist = i
                break

    rooms[exist] -= 1
    rooms[blank] += 1
    dist[blank] += d + dist[exist]
    dist[exist] = 0

print(sum(map(lambda x: x * x, dist)))
