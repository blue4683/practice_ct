import sys
input = sys.stdin.readline


def fold(start, end):
    if start == end:
        return 1

    mid = (start + end) // 2
    for i in range(start, mid):
        if paper[i] == paper[end - i]:
            return 0

    return fold(start, mid - 1) and fold(mid + 1, end)


for _ in range(int(input())):
    paper = input().rstrip()
    print('YES') if fold(0, len(paper) - 1) else print('NO')
