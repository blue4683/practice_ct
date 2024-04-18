import math
import sys
input = sys.stdin.readline


def init(start, end, index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]

    mid = (start + end) // 2
    tree[index] = init(start, mid, index * 2) + \
        init(mid + 1, end, index * 2 + 1)
    return tree[index]


def query(start, end, index, left, right):
    if left > end or right < start:
        return 0

    if left <= start and right >= end:
        return tree[index]

    mid = (start + end) // 2
    return query(start, mid, index * 2, left, right) + query(mid + 1, end, index * 2 + 1, left, right)


def update(start, end, index, node, value):
    if node < start or node > end:
        return tree[index]

    if start == end:
        tree[index] = value
        return tree[index]

    mid = (start + end) // 2
    l, r = update(start, mid, index * 2, node,
                  value), update(mid + 1, end, index * 2 + 1, node, value)
    tree[index] = l + r
    return tree[index]


n, q = map(int, input().split())
arr = list(map(int, input().split()))
tree_size = 1 << (math.ceil(math.log2(n) + 1) + 1)
tree = [0] * tree_size
init(0, n - 1, 1)

for _ in range(q):
    x, y, a, b = map(int, input().split())
    if x > y:
        x, y = y, x

    print(query(0, n - 1, 1, x - 1, y - 1))
    update(0, n - 1, 1, a - 1, b)
