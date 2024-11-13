import sys
input = sys.stdin.readline


def get_relations(arr):
    for mid in range(1, n + 1):
        for start in range(1, n + 1):
            for end in range(1, n + 1):
                if arr[start][end]:
                    continue

                arr[start][end] = arr[start][mid] and arr[mid][end]

    return arr


n = int(input())
big = [[0] * (n + 1) for _ in range(n + 1)]
small = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    big[a][b] = 1
    small[b][a] = 1

big = get_relations(big)
small = get_relations(small)

result = [n - 1 - sum(big[y]) - sum(small[y]) for y in range(1, n + 1)]
for res in result:
    print(res)
