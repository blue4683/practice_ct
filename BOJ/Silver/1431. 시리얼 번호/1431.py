import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    serial = input().rstrip()
    v = 0
    for c in serial:
        if c.isnumeric():
            v += int(c)

    arr.append((len(serial), v, serial))

arr.sort()
for _, _, serial in arr:
    print(serial)
