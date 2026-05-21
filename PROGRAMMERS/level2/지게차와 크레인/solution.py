def solution(storage, requests):
    n, m = len(storage), len(storage[0])
    answer = n * m
    tmp = [['0'] * (m + 2)]
    for l in storage:
        tmp.append(['0'] + list(l) + ['0'])

    tmp.append(['0'] * (m + 2))
    storage = tmp
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def out_of_range(y, x):
        if y < 0 or y >= n + 2 or x < 0 or x >= m + 2:
            return 1

        return 0

    def check():
        q = [(0, 0)]
        visited = [[0] * (m + 2) for _ in range(n + 2)]
        visited[0][0] = 1
        while q:
            y, x = q.pop()
            for dy, dx in d:
                yy, xx = y + dy, x + dx
                if out_of_range(yy, xx) or visited[yy][xx] or storage[yy][xx] not in {'0', '1'}:
                    continue

                visited[yy][xx] = 1
                if storage[yy][xx] == '0':
                    q.append((yy, xx))

                elif storage[yy][xx] == '1':
                    storage[yy][xx] = '0'
                    q.append((yy, xx))

    def use_forklift(container):
        q = [(0, 0)]
        visited = [[0] * (m + 2) for _ in range(n + 2)]
        visited[0][0] = 1
        cnt = 0
        while q:
            y, x = q.pop()
            for dy, dx in d:
                yy, xx = y + dy, x + dx
                if out_of_range(yy, xx) or visited[yy][xx]:
                    continue

                visited[yy][xx] = 1
                if storage[yy][xx] == '0':
                    q.append((yy, xx))

                elif storage[yy][xx] == container:
                    storage[yy][xx] = '0'
                    cnt += 1

        return cnt

    def use_crain(container):
        containers = [(y, x) for y in range(1, n + 1)
                      for x in range(1, m + 1) if storage[y][x] == container]
        for y, x in containers:
            storage[y][x] = '1'

        return len(containers)

    for request in requests:
        if len(request) == 2:
            answer -= use_crain(request[0])

        else:
            answer -= use_forklift(request[0])

        check()

    return answer
