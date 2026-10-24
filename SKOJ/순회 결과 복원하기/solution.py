import sys
sys.setrecursionlimit(10 ** 6)


def trace(pre_start, in_start, in_end):
    if in_start >= in_end:
        return

    root = preorder[pre_start]
    idx = pos[root]
    left_size = idx - in_start

    trace(pre_start + 1, in_start, idx)
    trace(pre_start + 1 + left_size, idx + 1, in_end)

    print(root, end=' ')


n = int(input())
preorder = list(map(int, input().split()))
inorder = list(map(int, input().split()))
pos = {value: idx for idx, value in enumerate(inorder)}
trace(0, 0, n)
