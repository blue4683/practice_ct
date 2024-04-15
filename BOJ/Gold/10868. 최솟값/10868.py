import math
import sys
input = sys.stdin.readline


def init(start, end, index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]

    mid = (start + end) // 2
    l, r = init(start, mid, index * 2), init(mid + 1, end, index * 2 + 1)
    tree[index] = min(l, r)

    return tree[index]


def query(start, end, index, left, right):
    if left > end or right < start:
        return 10 ** 9

    if left <= start and right >= end:
        return tree[index]

    mid = (start + end) // 2
    l, r = query(start, mid, index * 2, left, right), query(mid +
                                                            1, end, index * 2 + 1, left, right)
    return min(l, r)


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

tree_size = 1 << (math.ceil(math.log2(n)) + 1)
tree = [0] * tree_size
init(0, n - 1, 1)

for _ in range(m):
    a, b = map(int, input().split())
    print(query(0, n - 1, 1, a - 1, b - 1))
