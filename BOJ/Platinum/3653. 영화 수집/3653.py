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
    if start > right or end < left:
        return 0

    if left <= start and right >= end:
        return tree[index]

    mid = (start + end) // 2
    return query(start, mid, index * 2, left, right) + query(mid + 1, end, index * 2 + 1, left, right)


def update(start, end, index, node, value):
    if start > node or end < node:
        return tree[index]

    if start == end:
        tree[index] = value
        return tree[index]

    mid = (start + end) // 2
    tree[index] = update(start, mid, index * 2, node, value) + \
        update(mid + 1, end, index * 2 + 1, node, value)
    return tree[index]


for _ in range(int(input())):
    n, m = map(int, input().split())
    size = n + m - 1
    arr = [0] * (size + 1)
    for i in range(n):
        arr[i] = 1

    tree_size = 1 << (math.ceil(math.log2(size + 1)) + 1)
    tree = [0] * tree_size
    init(0, size, 1)

    for i in range(1, n + 1):
        arr[i] = n - i

    result = []
    for data in map(int, input().split()):
        result.append(query(0, size, 1, arr[data] + 1, size))
        update(0, size, 1, arr[data], 0)
        n += 1
        update(0, size, 1, n, 1)
        arr[data] = n

    print(*result)
