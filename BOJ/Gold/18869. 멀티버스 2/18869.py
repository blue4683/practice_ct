from collections import defaultdict
import sys
input = sys.stdin.readline


def bisect(x, arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > x:
            right = mid - 1

        elif arr[mid] < x:
            left = mid + 1

        else:
            left = mid
            break

    return left


m, n = map(int, input().split())
universe = defaultdict(int)

for _ in range(m):
    galaxy = list(map(int, input().split()))
    arr = sorted(galaxy)
    rank = []
    for planet in galaxy:
        rank.append(bisect(planet, arr))

    universe[tuple(rank)] += 1

result = 0
for k in universe.values():
    result += ((k - 1) * k) // 2

print(result)
