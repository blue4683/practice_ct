import sys
input = sys.stdin.readline
INF = 10 ** 9


def connect(number):
    if visited[number]:
        return

    visited[number] = 1
    for next_number in graph[number]:
        connect(next_number)
        employers[number].add(next_number)
        employers[number].update(employers[next_number])


n, m, i = map(int, input().split())
ages = [0] + list(map(int, input().split()))
graph = [set() for _ in range(n + 1)]
for _ in range(m):
    employer, employee = map(int, input().split())
    graph[employee].add(employer)

employers = [set() for _ in range(n + 1)]
visited = [0] * (n + 1)
for number in range(1, n + 1):
    connect(number)

employees = list(range(n + 1))
pos = list(range(n + 1))

for _ in range(i):
    args = input().split()
    if args[0] == 'P':
        target = pos[int(args[1])]
        result = INF
        for number in employers[target]:
            result = min(result, ages[employees[number]])

        print(result) if result != INF else print('*')

    else:
        a, b = map(int, args[1:])
        pos[a], pos[b] = pos[b], pos[a]
        employees[pos[a]] = a
        employees[pos[b]] = b
