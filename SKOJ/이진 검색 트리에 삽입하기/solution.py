INF = -10 ** 9

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
        
def insert(root, value):
    if root == None:
        return Node(value)
    
    cur = root
    while 1:
        if value < cur.val:
            if cur.left is None:
                cur.left = Node(value)
                return root
            
            cur = cur.left
            
        else:
            if cur.right is None:
                cur.right = Node(value)
                return root

            cur = cur.right
            

def inorder(root):
    result = []
    stack = []
    cur = root
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
            
        cur = stack.pop()
        result.append(cur.val)
        cur = cur.right
    
    return result


n = int(input())
arr = list(map(int, input().split()))

root = None
for num in arr:
    root = insert(root, num)
    
result = inorder(root)
print(*result)
