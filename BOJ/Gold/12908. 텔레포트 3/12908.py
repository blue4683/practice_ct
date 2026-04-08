import sys
input = sys.stdin.readline
INF = 10 ** 9


def get_dist(i, j):
    x1, y1 = pos[i]
    x2, y2 = pos[j]
    return abs(x1 - x2) + abs(y1 - y2)


pos = [tuple(map(int, input().split())) for _ in range(2)]
for _ in range(3):
    x1, y1, x2, y2 = map(int, input().split())
    pos.append((x1, y1))
    pos.append((x2, y2))

arr = [[INF] * 8 for _ in range(8)]
for i in range(8):
    for j in range(8):
        a, b = i // 2, j // 2
        dist = get_dist(i, j)
        if a and b and a == b:
            arr[i][j] = min(dist, 10)
            arr[j][i] = min(dist, 10)

        else:
            arr[i][j] = dist

for mid in range(8):
    for s in range(8):
        for e in range(8):
            if arr[s][mid] + arr[mid][e] < arr[s][e]:
                arr[s][e] = arr[s][mid] + arr[mid][e]

print(arr[0][1])
