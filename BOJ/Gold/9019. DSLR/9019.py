from collections import defaultdict, deque
import sys
input = sys.stdin.readline
commands = 'DSLR'


def run_command(n, command):
    if command == 'D':
        return str((int(n) * 2) % 10000).zfill(4)

    elif command == 'S':
        return '9999' if n == '0000' else str(int(n) - 1).zfill(4)

    elif command == 'L':
        return n[1:] + n[0]

    else:
        return n[-1] + n[:-1]


def bfs():
    visited = defaultdict(int)
    visited[a] = 1
    q = deque([(a, '')])
    while q:
        n, c = q.popleft()
        for command in commands:
            nn = run_command(n, command)
            if visited[nn]:
                continue

            if nn == b:
                return c + command

            visited[nn] = 1
            q.append((nn, c + command))

    return ''


for _ in range(int(input())):
    a, b = map(lambda x: x.zfill(4), input().split())
    print(bfs())
