import sys
input = sys.stdin.readline


def copy_arr(arr):
    new_arr = []
    for l in arr:
        new_arr.append(l[:])

    return new_arr


def play(arr, i):
    if i == 0:
        for y in range(n):
            cursor = 0
            for x in range(1, n):
                if arr[y][x] != 0:
                    tmp = arr[y][x]
                    arr[y][x] = 0

                    if arr[y][cursor] == 0:
                        arr[y][cursor] = tmp

                    elif arr[y][cursor] == tmp:
                        arr[y][cursor] *= 2
                        cursor += 1

                    else:
                        cursor += 1
                        arr[y][cursor] = tmp

    elif i == 1:
        for y in range(n):
            cursor = n - 1
            for x in range(n - 1, -1, -1):
                if arr[y][x] != 0:
                    tmp = arr[y][x]
                    arr[y][x] = 0

                    if arr[y][cursor] == 0:
                        arr[y][cursor] = tmp

                    elif arr[y][cursor] == tmp:
                        arr[y][cursor] *= 2
                        cursor -= 1

                    else:
                        cursor -= 1
                        arr[y][cursor] = tmp

    elif i == 2:
        for x in range(n):
            cursor = 0
            for y in range(1, n):
                if arr[y][x] != 0:
                    tmp = arr[y][x]
                    arr[y][x] = 0

                    if arr[cursor][x] == 0:
                        arr[cursor][x] = tmp

                    elif arr[cursor][x] == tmp:
                        arr[cursor][x] *= 2
                        cursor += 1

                    else:
                        cursor += 1
                        arr[cursor][x] = tmp

    else:
        for x in range(n):
            cursor = n - 1
            for y in range(n - 1, -1, -1):
                if arr[y][x] != 0:
                    tmp = arr[y][x]
                    arr[y][x] = 0

                    if arr[cursor][x] == 0:
                        arr[cursor][x] = tmp

                    elif arr[cursor][x] == tmp:
                        arr[cursor][x] *= 2
                        cursor -= 1

                    else:
                        cursor -= 1
                        arr[cursor][x] = tmp

    return arr


def dfs(depth, arr):
    global result
    if depth == 5:
        result = max(result, max(map(lambda x: max(x), arr)))
        return

    for i in range(4):
        new_arr = play(copy_arr(arr), i)
        dfs(depth + 1, new_arr)


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
result = 0
dfs(0, board)

print(result)
