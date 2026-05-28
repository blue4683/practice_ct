from collections import deque


def solution(points, routes):
    answer = 0
    q = deque()
    start = set()
    collided = set()
    for route in routes:
        if route[0] in start and route[0] not in collided:
            answer += 1
            collided.add(route[0])

        else:
            start.add(route[0])

        sr, sc = points[route[0] - 1]
        q.append((sr, sc, route[1:][::-1]))

    while 1:
        moved = deque()
        moved_pos = set()
        collided = set()
        while q:
            r, c, dests = q.popleft()
            er, ec = points[dests[-1] - 1]
            if er != r:
                r = r + 1 if er > r else r - 1

            else:
                c = c + 1 if ec > c else c - 1

            if (r, c) in moved_pos and (r, c) not in collided:
                answer += 1
                collided.add((r, c))

            elif (r, c) not in moved_pos:
                moved_pos.add((r, c))

            if (r, c) == (er, ec):
                dests.pop()

            if dests:
                moved.append((r, c, dests))

        if not moved:
            break

        q = moved

    return answer
