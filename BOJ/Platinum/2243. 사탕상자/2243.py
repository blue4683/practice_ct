import math
import sys
input = sys.stdin.readline


def query(start, end, index, node):
    if start == end:
        return start

    mid = (start + end) // 2
    if node <= tree[index * 2]:
        return query(start, mid, index * 2, node)

    else:
        return query(mid + 1, end, index * 2 + 1, node - tree[index * 2])


def update(start, end, index, node, value):
    if node < start or node > end:
        return tree[index]

    if start == end:
        tree[index] += value
        return tree[index]

    mid = (start + end) // 2
    l = update(start, mid, index * 2, node, value)
    r = update(mid + 1, end, index * 2 + 1, node, value)
    tree[index] = l + r
    return tree[index]


n = int(input())
MAX = 10 ** 6 + 1
tree_size = 1 << (math.ceil(math.log2(MAX)) + 1)
tree = [0] * tree_size

for _ in range(n):
    order, *args = map(int, input().split())
    if order == 1:
        candy = query(1, MAX, 1, args[0])
        print(candy)
        update(1, MAX, 1, candy, -1)

    else:
        b, c = args
        update(1, MAX, 1, b, c)
