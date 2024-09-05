import sys
input = sys.stdin.readline


def set_limit(game):
    max_size = 0
    if game == 'Y':
        max_size = 1

    elif game == 'F':
        max_size = 2

    else:
        max_size = 3

    return max_size


n, game = input().split()
n = int(n)

max_size = set_limit(game)
visited = dict()
queue = []
result = 0

for player in [input().rstrip() for _ in range(n)]:
    if player in visited or player in queue:
        continue

    queue.append(player)
    if len(queue) == max_size:
        while queue:
            visited[queue.pop()] = 1

        result += 1

print(result)
