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


def update_lazy(start, end, index):
    if lazy[index]:
        tree[index] += (end - start + 1) * lazy[index]
        if start != end:
            lazy[index * 2] += lazy[index]
            lazy[index * 2 + 1] += lazy[index]

        lazy[index] = 0


def query(start, end, index, left, right):
    update_lazy(start, end, index)
    if left > end or right < start:
        return 0

    if left <= start and right >= end:
        return tree[index]

    mid = (start + end) // 2
    return query(start, mid, index * 2, left, right) + query(mid + 1, end, index * 2 + 1, left, right)


def update_range(start, end, index, left, right, value):
    update_lazy(start, end, index)
    if left > end or right < start:
        return tree[index]

    if left <= start and right >= end:
        tree[index] += (end - start + 1) * value
        if start != end:
            lazy[index * 2] += value
            lazy[index * 2 + 1] += value

        return tree[index]

    mid = (start + end) // 2
    tree[index] = update_range(start, mid, index * 2, left, right, value) + \
        update_range(mid + 1, end, index * 2 + 1, left, right, value)
    return tree[index]


n = int(input())
arr = list(map(int, input().split()))
tree_size = 1 << (math.ceil(math.log2(n)) + 1)
tree = [0] * tree_size
lazy = [0] * tree_size
init(0, n - 1, 1)

m = int(input())
for _ in range(m):
    order, *args = map(int, input().split())
    if order == 1:
        i, j, k = args
        update_range(0, n - 1, 1, i - 1, j - 1, k)

    else:
        x = args[0]
        print(query(0, n - 1, 1, x - 1, x - 1))
