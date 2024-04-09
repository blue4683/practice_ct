import math
import sys
input = sys.stdin.readline


def query(start, end, index, left, right):
    if start > right or end < left:
        return 0

    if left <= start and right >= end:
        return tree[index]

    mid = (start + end) // 2
    return query(start, mid, index * 2, left, right) + query(mid + 1, end, index * 2 + 1, left, right)


def update(start, end, index, node):
    if start > node or end < node:
        return

    if start == end:
        tree[index] += 1
        return

    tree[index] += 1
    mid = (start + end) // 2
    update(start, mid, index * 2, node)
    update(mid + 1, end, index * 2 + 1, node)


n = int(input())
plant = dict()
connect = [0] * (n + 1)

for index, number in enumerate(map(int, input().split())):
    plant[number] = index

for index, number in enumerate(map(int, input().split())):
    pos = plant[number]
    connect[pos] = index

tree_size = 1 << (math.ceil(math.log2(n)) + 1)
tree = [0] * tree_size

result = 0
for i in range(n):
    pos = connect[i]
    result += query(0, n - 1, 1, pos + 1, n)
    update(0, n - 1, 1, pos)

print(result)
