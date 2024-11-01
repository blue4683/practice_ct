import sys
input = sys.stdin.readline


def get_distance(a, b):
    y1, x1 = checkpoints[a]
    y2, x2 = checkpoints[b]
    return abs(y1 - y2) + abs(x1 - x2)


n = int(input())
checkpoints = [tuple(map(int, input().split())) for _ in range(n)]
distance = 0
for i in range(n - 1):
    distance += get_distance(i, i + 1)

result = 10 ** 9
for skipped in range(1, n - 1):
    result = min(result, distance - get_distance(skipped - 1, skipped) -
                 get_distance(skipped, skipped + 1) + get_distance(skipped - 1, skipped + 1))

print(result)
