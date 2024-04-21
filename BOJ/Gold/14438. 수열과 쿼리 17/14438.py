import math
import sys
input = sys.stdin.readline


def init(start, end, index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    
    mid = (start + end) // 2
    tree[index] = min(init(start, mid, index * 2), init(mid + 1, end, index * 2 + 1))
    return tree[index]


def query(start, end, index, left, right):
    if right < start or left > end:
        return 10 ** 9
    
    if left <= start and right >= end:
        return tree[index]
    
    mid = (start + end) // 2
    return min(query(start, mid, index * 2, left, right), query(mid + 1, end, index * 2 + 1, left, right))


def update(start, end, index, node, value):
    if node < start or node > end:
        return tree[index]
    
    if start == end:
        tree[index] = value
        return tree[index]
    
    mid = (start + end) // 2
    tree[index] = min(update(start, mid, index * 2, node, value), update(mid + 1, end, index * 2 + 1, node, value))
    return tree[index]


n = int(input())
arr = list(map(int, input().split()))
tree_size = 1 << (math.ceil(math.log2(n)) + 1)
tree = [0] * tree_size
init(0, n - 1, 1)

m = int(input())
for _ in range(m):
    order, *args = map(int, input().split())
    if order == 1:
        i, v = args
        update(0, n - 1, 1, i - 1, v)

    else:
        i, j = args
        if i > j:
            i, j = j, i

        print(query(0, n - 1, 1, i - 1, j - 1))
