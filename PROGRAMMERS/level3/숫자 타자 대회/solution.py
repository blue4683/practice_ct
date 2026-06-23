from collections import defaultdict, deque
from heapq import heappop, heappush


def get_weight(a, b, pos):
    if a == b:
        return 1

    ay, ax = pos[a]
    by, bx = pos[b]

    dy = abs(ay - by)
    dx = abs(ax - bx)

    if dy + dx == 1:
        return 2

    if dy == 1 and dx == 1:
        return 3

    return 10 ** 9


def solution(numbers):
    answer = 0
    n = len(numbers)
    INF = 10 ** 9
    pos = {
        '1': (0, 0), '2': (0, 1), '3': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '7': (2, 0), '8': (2, 1), '9': (2, 2),
        '0': (3, 1),
    }

    keys = pos.keys()
    dist = {key: defaultdict(lambda: INF) for key in keys}
    for key in keys:
        q = deque([(key, 0)])
        dist[key][key] = 1
        while q:
            x, c = q.popleft()
            for xx in keys:
                cc = get_weight(x, xx, pos)
                if c + cc < dist[key][xx]:
                    dist[key][xx] = c + cc
                    q.append((xx, dist[key][xx]))

    visited = defaultdict(lambda: INF)
    heap = [(0, 0, '4', '6')]
    while heap:
        cost, depth, l, r = heappop(heap)
        if depth == n:
            answer = cost
            break

        if visited[(depth, l, r)] <= cost:
            continue

        visited[(depth, l, r)] = cost
        t = numbers[depth]
        if r != t:
            heappush(heap, (cost + dist[l][t], depth + 1, t, r))

        if l != t:
            heappush(heap, (cost + dist[t][r], depth + 1, l, t))

    return answer
