import sys
import math
input = sys.stdin.readline


def init(start, end, index):
    if start == end:
        tree[index] = (arr[start], arr[start])
        return tree[index]

    mid = (start + end) // 2
    l, r = init(start, mid, index * 2), init(mid + 1, end, index * 2 + 1)

    tree[index] = (min(l[0], r[0]), max(l[1], r[1]))
    return tree[index]


def get(start, end, index, left, right):
    if left > end or right < start:
        return (10 ** 9, 0)

    if left <= start and right >= end:
        return tree[index]

    mid = (start + end) // 2
    l, r = get(start, mid, index * 2, left, right), get(mid +
                                                        1, end, index * 2 + 1, left, right)
    return (min(l[0], r[0]), max(l[1], r[1]))


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
tree_size = 1 << (math.ceil(math.log2(n)) + 1)
tree = [0] * tree_size

init(0, n - 1, 1)

for _ in range(m):
    a, b = map(int, input().split())
    print(*get(0, n - 1, 1, a - 1, b - 1))
