from collections import defaultdict
import sys
input = sys.stdin.readline


while 1:
    n, k = map(int, input().split())
    if (n, k) == (0, 0):
        break

    arr = list(map(int, input().split()))

    parents = defaultdict(int)
    idx = -1
    for i in range(1, n):
        node = arr[i]
        if node - arr[i - 1] != 1:
            idx += 1

        parents[node] = arr[idx]

    result = 0
    if parents[parents[k]]:
        for node in arr:
            if parents[node] != parents[k] and parents[parents[node]] == parents[parents[k]]:
                result += 1

    print(result)
