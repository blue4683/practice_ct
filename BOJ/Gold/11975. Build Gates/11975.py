import sys
input = sys.stdin.readline

d = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}

n = int(input())
directions = input().rstrip()
visedge = set()
visnode = set()
result = 0
prev = (0, 0)
visnode.add(prev)

for i in range(n):
    y, x = prev
    dy, dx = d[directions[i]]
    y += dy
    x += dx

    if ((y, x), prev) not in visedge and (y, x) in visnode:
        result += 1

    visedge.add(((y, x), prev))
    visedge.add((prev, (y, x)))
    visnode.add((y, x))

    prev = (y, x)

print(result)
