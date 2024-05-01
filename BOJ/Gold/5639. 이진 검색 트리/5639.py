import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def postorder(start, end):
    if start > end:
        return

    right = start + 1
    for i in range(start + 1, end + 1):
        if preorder[start] < preorder[i]:
            right = i
            break

    postorder(start + 1, right - 1)
    postorder(right, end)
    print(preorder[start])


preorder = []
while 1:
    try:
        preorder.append(int(input()))

    except:
        break

postorder(0, len(preorder) - 1)
