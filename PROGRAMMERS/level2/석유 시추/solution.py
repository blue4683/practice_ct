def solution(land):
    answer = 0
    n, m = len(land), len(land[0])
    visited = [[[] for _ in range(m)] for _ in range(n)]
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def find(sy, sx, num):
        q = [(sy, sx)]
        v = {(sy, sx)}
        while q:
            y, x = q.pop()
            for dy, dx in d:
                yy, xx = y + dy, x + dx
                if yy < 0 or yy >= n or xx < 0 or xx >= m or not land[yy][xx] or (yy, xx) in v:
                    continue

                v.add((yy, xx))
                q.append((yy, xx))

        cnt = len(v)
        for y, x in v:
            visited[y][x] = [cnt, num]

    num = 1
    for y in range(n):
        for x in range(m):
            if land[y][x] and not visited[y][x]:
                find(y, x, num)
                num += 1

    for x in range(m):
        v = set()
        total = 0
        for y in range(n):
            if visited[y][x] and visited[y][x][1] not in v:
                v.add(visited[y][x][1])
                total += visited[y][x][0]

        answer = max(answer, total)

    return answer
