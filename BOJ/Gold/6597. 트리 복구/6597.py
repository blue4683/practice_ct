import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def postorder(preorder, inorder):
    if not preorder or not inorder:
        return []

    root = preorder[0]
    index = inorder.index(root)

    left_in, right_in = inorder[:index], inorder[index + 1:]
    left_pre, right_pre = preorder[1:len(
        left_in) + 1], preorder[len(left_in) + 1:]

    return postorder(left_pre, left_in) + postorder(right_pre, right_in) + [root]


while 1:
    try:
        preorder, inorder = input().split()

    except:
        break

    print(''.join(postorder(preorder, inorder)))
