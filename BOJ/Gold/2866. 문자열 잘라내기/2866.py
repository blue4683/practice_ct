from collections import defaultdict
import sys
input = sys.stdin.readline


def check(mid) -> bool:
    for i in range(c):
        string = ''
        for j in range(mid, r):
            string += words[j][i]

        if table[string]:
            return 0

        table[string] += 1

    return 1


r, c = map(int, input().split())
words = [input().rstrip() for _ in range(r)]

result = 0
start, end = 0, r - 1
while start <= end:
    mid = (start + end) // 2
    table = defaultdict(int)
    if check(mid):
        result = mid
        start = mid + 1

    else:
        end = mid - 1

print(result)
