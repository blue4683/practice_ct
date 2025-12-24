import sys
input = sys.stdin.readline


def dfs(depth, i):
    global result
    if result:
        return

    if depth == 15:
        if not sum(map(sum, arr[i])):
            result = 1

        return

    a, b = matches[depth]
    if arr[i][a][0] and arr[i][b][2]:
        arr[i][a][0] -= 1
        arr[i][b][2] -= 1
        dfs(depth + 1, i)
        arr[i][a][0] += 1
        arr[i][b][2] += 1

    if arr[i][a][1] and arr[i][b][1]:
        arr[i][a][1] -= 1
        arr[i][b][1] -= 1
        dfs(depth + 1, i)
        arr[i][a][1] += 1
        arr[i][b][1] += 1

    if arr[i][a][2] and arr[i][b][0]:
        arr[i][a][2] -= 1
        arr[i][b][0] -= 1
        dfs(depth + 1, i)
        arr[i][a][2] += 1
        arr[i][b][0] += 1


arr = [list(map(int, input().split())) for _ in range(4)]
arr = [[arr[j][i:i + 3] for i in range(0, 18, 3)] for j in range(4)]

r = []
matches = [(x, y) for x in range(6) for y in range(x + 1, 6)]
for i in range(4):
    result = 0
    dfs(0, i)
    r.append(result)

print(*r)
