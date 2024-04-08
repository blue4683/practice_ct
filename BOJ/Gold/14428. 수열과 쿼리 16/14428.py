import sys
import math
input = sys.stdin.readline


def init(start, end, index):
    if start == end:
        tree[index] = (arr[start], start)
        return tree[index]

    mid = (start + end) // 2
    l, r = init(start, mid, index * 2), init(mid + 1, end, index * 2 + 1)

    tree[index] = min(l, r)
    return tree[index]


def get(start, end, index, left, right):
    if left > end or right < start:
        return (10 ** 9, 10 ** 9)

    if left <= start and right >= end:
        return tree[index]

    mid = (start + end) // 2
    l, r = get(start, mid, index * 2, left, right), get(mid +
                                                        1, end, index * 2 + 1, left, right)
    return min(l, r)


def update(start, end, index, node, value):
    if node < start or node > end:
        return tree[index]

    if start == end:
        tree[index] = (value, node)
        return tree[index]

    mid = (start + end) // 2
    l = update(start, mid, index * 2, node, value)
    r = update(mid + 1, end, index * 2 + 1, node, value)
    tree[index] = min(l, r)
    return tree[index]


n = int(input())
arr = list(map(int, input().split()))
tree_size = 1 << (math.ceil(math.log2(n)) + 1)
tree = [0] * tree_size

init(0, n - 1, 1)

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    if a == 1:
        value = c
        arr[b - 1] = c
        update(0, n - 1, 1, b - 1, value)

    else:
        print(get(0, n - 1, 1, b - 1, c - 1)[1] + 1)
