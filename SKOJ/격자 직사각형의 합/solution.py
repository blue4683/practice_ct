h, w, q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]

prefix = [[0] * (w + 1) for _ in range(h + 1)]
for y in range(1, h + 1):
    prefix[y][1] = prefix[y - 1][1] + arr[y - 1][0]
    
for x in range(1, w + 1):
    prefix[1][x] = prefix[1][x - 1] + arr[0][x - 1]
    
for y in range(1, h + 1):
    for x in range(1, w + 1):
        prefix[y][x] = prefix[y - 1][x] + prefix[y][x - 1] - prefix[y - 1][x - 1] + arr[y - 1][x - 1]

for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    print(prefix[r2][c2] - prefix[r1 - 1][c2] - prefix[r2][c1 - 1] + prefix[r1 - 1][c1 - 1])
