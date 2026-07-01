def solution(commands):
    answer = []
    graph = [i for i in range(50 * 50)]
    cells = ['EMPTY'] * (50 * 50)

    def find(x):
        if x != graph[x]:
            graph[x] = find(graph[x])

        cells[x] = cells[graph[x]]
        return graph[x]

    def union(x, y):
        x, y = find(x), find(y)
        graph[y] = x
        if cells[x] != 'EMPTY':
            cells[y] = cells[x]

        elif cells[x] == 'EMPTY' and cells[y] != 'EMPTY':
            cells[x] = cells[y]

    for command in commands:
        command, *args = command.split()
        if command == 'UPDATE':
            if len(args) == 3:
                r, c, value = args
                r, c = int(r) - 1, int(c) - 1
                n = r * 50 + c
                cells[find(n)] = value
                for i in range(50 * 50):
                    if find(i) == find(n):
                        cells[i] = value

            else:
                value1, value2 = args
                for i in range(50 * 50):
                    if cells[i] == value1:
                        cells[i] = value2

        elif command == 'MERGE':
            r1, c1, r2, c2 = args
            r1, c1 = int(r1) - 1, int(c1) - 1
            r2, c2 = int(r2) - 1, int(c2) - 1
            n1, n2 = r1 * 50 + c1, r2 * 50 + c2
            wait = []
            for i in range(50 * 50):
                if find(i) == find(n2):
                    wait.append(i)

            for i in wait:
                union(n1, i)

        elif command == 'UNMERGE':
            r, c = args
            r, c = int(r) - 1, int(c) - 1
            n = r * 50 + c
            value = cells[find(n)]
            wait = []
            for i in range(50 * 50):
                if find(i) == find(n):
                    wait.append(i)

            for i in wait:
                graph[i] = i
                if i != n:
                    cells[i] = 'EMPTY'

                else:
                    cells[i] = value

        else:
            r, c = args
            r, c = int(r) - 1, int(c) - 1
            n = r * 50 + c
            answer.append(cells[find(n)])

    return answer
