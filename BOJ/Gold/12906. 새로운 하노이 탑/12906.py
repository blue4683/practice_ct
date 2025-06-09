from collections import defaultdict, deque
import sys
input = sys.stdin.readline


def is_end(arr):
    for i in range(3):
        if arr[i] == '' or set([chr(ord('A') + i)]) == set(arr[i]):
            continue

        return 0

    return 1


def bfs():
    visited = defaultdict(int)
    visited[sticks] = 1
    q = deque([sticks[:]])
    while q:
        arr = q.popleft()
        if is_end(arr):
            return visited[arr] - 1

        for i in range(3):
            if arr[i] == '' or set([chr(ord('A') + i)]) == set(arr[i]):
                continue

            for j in range(3):
                if i == j:
                    continue

                tmp = list(arr)
                tmp[j] = tmp[j] + tmp[i][-1]
                tmp[i] = tmp[i][:-1]
                if visited[tuple(tmp)]:
                    continue

                visited[tuple(tmp)] = visited[arr] + 1
                q.append(tuple(tmp))

    return -1


sticks = []
for _ in range(3):
    params = input().split()
    if len(params) == 2:
        sticks.append(params[1])

    else:
        sticks.append('')

sticks = tuple(sticks)
print(bfs())
