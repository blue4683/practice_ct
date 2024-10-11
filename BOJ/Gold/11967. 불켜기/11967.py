from collections import defaultdict, deque
import sys
input = sys.stdin.readline

d = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_range(y, x):
    if y < 1 or y > n or x < 1 or x > n:
        return 1

    return 0


def bfs():
    result = 1
    q = deque([(1, 1)])
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    visited = [[0] * (n + 1) for _ in range(n + 1)]
    graph[1][1] = 1
    visited[1][1] = 1
    while q:
        y, x = q.popleft()
        if not graph[y][x]:
            continue

        if (y, x) in rooms.keys():
            for b, a in rooms[(y, x)]:
                if graph[b][a]:
                    continue

                graph[b][a] = 1
                for db, da in d:
                    bb, aa = b + db, a + da
                    if out_of_range(bb, aa) or not visited[bb][aa]:
                        continue

                    q.appendleft((bb, aa))
                    break

                result += 1

        for dy, dx in d:
            yy, xx = y + dy, x + dx
            if out_of_range(yy, xx) or visited[yy][xx]:
                continue

            if graph[yy][xx]:
                visited[yy][xx] = 1
                q.appendleft((yy, xx))

            else:
                q.append((yy, xx))

    return result


n, m = map(int, input().split())
rooms = defaultdict(list)
for _ in range(m):
    x, y, a, b = map(int, input().split())
    rooms[(y, x)].append((b, a))

print(bfs())
