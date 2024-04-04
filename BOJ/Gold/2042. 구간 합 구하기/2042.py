import sys
import math
input = sys.stdin.readline


def init(start, end, idx):
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]

    mid = (start + end) // 2
    tree[idx] = init(start, mid, idx * 2) + init(mid + 1, end, idx * 2 + 1)
    return tree[idx]


def get_sum(start, end, idx, left, right):
    if left > end or right < start:
        return 0

    if left <= start and right >= end:
        return tree[idx]

    mid = (start + end) // 2
    return get_sum(start, mid, idx * 2, left, right) + get_sum(mid + 1, end, idx * 2 + 1, left, right)


def update(start, end, idx, node, value):
    if node < start or node > end:
        return

    tree[idx] += value
    if start == end:
        return

    mid = (start + end) // 2
    update(start, mid, idx * 2, node, value)
    update(mid + 1, end, idx * 2 + 1, node, value)


n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
tree = [0] * (4 * n)
init(0, n - 1, 1)

for _ in range(m + k):
    a, b, c = map(int, input().split())

    if a == 1:
        value = c - arr[b - 1]
        arr[b - 1] = c
        update(0, n - 1, 1, b - 1, value)

    else:
        print(get_sum(0, n - 1, 1, b - 1, c - 1))
