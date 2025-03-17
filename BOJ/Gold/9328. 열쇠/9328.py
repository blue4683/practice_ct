from collections import defaultdict, deque
import sys
input = sys.stdin.readline
d = [(0, 1), (-1, 0), (1, 0), (0, -1)]


def is_door(door):
    if ord('A') <= ord(door) <= ord('Z'):
        return 1

    return 0


def is_key(key):
    if ord('a') <= ord(key) <= ord('z'):
        return 1

    return 0


def out_of_range(y, x):
    if y < 0 or y >= h + 2 or x < 0 or x >= w + 2:
        return 1

    return 0


def bfs(keys):
    result = set()
    visited = defaultdict(int)
    visited[(0, 0)] = 1
    doors = set()
    q = deque([(0, 0)])
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[(yy, xx)] or arr[yy][xx] == '*':
                continue

            if arr[yy][xx] == '.':
                visited[(yy, xx)] = 1
                q.append((yy, xx))

            if is_door(arr[yy][xx]):
                visited[(yy, xx)] = 1
                if arr[yy][xx].lower() in keys:
                    q.append((yy, xx))

                else:
                    doors.add((yy, xx))

            elif is_key(arr[yy][xx]):
                visited[(yy, xx)] = 1
                if arr[yy][xx] not in keys:
                    keys.add(arr[yy][xx])
                    find = []
                    for yyy, xxx in doors:
                        if arr[yyy][xxx].lower() == arr[yy][xx]:
                            q.append((yyy, xxx))
                            find.append((yyy, xxx))

                    for yyy, xxx in find:
                        doors.discard((yyy, xxx))

                q.append((yy, xx))

            elif arr[yy][xx] == '$':
                visited[(yy, xx)] = 1
                q.append((yy, xx))
                if (yy, xx) not in result:
                    result.add((yy, xx))

    return len(result)


for _ in range(int(input())):
    h, w = map(int, input().split())
    arr = []
    for i in range(h + 2):
        if not i or i == h + 1:
            arr.append(['.'] * (w + 2))

        else:
            arr.append(list('.' + input().rstrip() + '.'))

    keys = set(list(input().rstrip()))
    print(bfs(keys))
