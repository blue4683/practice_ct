from collections import deque


def solution(m, n, h, w, drops):
    answer = []
    INF = 10 ** 9
    arr = [[INF] * n for _ in range(m)]
    for i in range(len(drops)):
        y, x = drops[i]
        arr[y][x] = i

    tmp = [[] for _ in range(n - w + 1)]
    for y in range(m):
        window = deque([])
        for x in range(n):
            while window and window[-1][1] > arr[y][x]:
                window.pop()

            window.append((x, arr[y][x]))
            if window[0][0] < x - w + 1:
                window.popleft()

            if x >= w - 1:
                tmp[x - w + 1].append(window[0][1])

    result = []
    for x in range(n - w + 1):
        window = deque()
        for y in range(m):
            while window and window[-1][1] > tmp[x][y]:
                window.pop()

            window.append((y, tmp[x][y]))
            if window[0][0] < y - h + 1:
                window.popleft()

            if y >= h - 1:
                result.append((window[0][1], y - h + 1, x))

    result.sort(key=lambda x: (-x[0], x[1], x[2]))
    answer = [*result[0][1:3]]
    return answer
