import sys
input = sys.stdin.readline

for _ in range(int(input())):
    w = input().rstrip()
    k = int(input())
    n = len(w)

    table = [[] for _ in range(26)]
    for i in range(n):
        table[ord(w[i]) - ord('a')].append(i)

    possible = [i for i in range(26) if len(table[i]) >= k]
    min_result = 10001
    max_result = -1

    for pos in possible:
        indexes = table[pos]
        m = len(indexes)
        for i in range(m - k + 1):
            min_result = min(min_result, indexes[i + k - 1] - indexes[i] + 1)
            max_result = max(max_result, indexes[i + k - 1] - indexes[i] + 1)

    print(min_result, max_result) if possible else print(-1)
