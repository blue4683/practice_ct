import math
import sys
input = sys.stdin.readline


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


n, m = map(int, input().split())
tree_size = 1 << (math.ceil(math.log2(n)) + 1)
tree = [0] * tree_size

for _ in range(m):
    order, *args = map(int, input().split())
    if order == 0:
        i, j = args
        if i > j:
            i, j = j, i

        print(query(0, n - 1, 1, i - 1, j - 1))

    else:
        i, k = args
        update(0, n - 1, 1, i - 1, k)
