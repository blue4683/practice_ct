from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = 10 ** 9


def dijkstra():
    heap = [(0, 0, a)]
    money, shame = [INF] * (n + 1), [INF] * (n + 1)
    money[a], shame[a] = 0, 0
    while heap:
        sh, mo, x = heappop(heap)
        if sh > shame[x]:
            continue

        for xx, mmo in graph[x]:
            if mmo + mo > c or max(sh, mmo) >= shame[xx]:
                continue

            money[xx] = mmo + mo
            shame[xx] = max(sh, mmo)
            heappush(heap, (shame[xx], money[xx], xx))

    return shame[b] if shame[b] != INF else -1


n, m, a, b, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))
    graph[y].append((x, z))

print(dijkstra())
