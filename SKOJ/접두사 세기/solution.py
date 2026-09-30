class Node():
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}
        self.cnt = 0
        
        
class Trie():
    def __init__(self):
        self.head = Node(None)
        
    def insert(self, string):
        cur = self.head
        for char in string:
            if char not in cur.children:
                cur.children[char] = Node(char)
                
            cur = cur.children[char]
            cur.cnt += 1
        
        cur.data = string
        
    def search(self, string):
        cur = self.head
        for char in string:
            if char not in cur.children:
                return 0
            
            cur = cur.children[char]
            
        return cur.cnt
    
n, m = map(int, input().split())
trie = Trie()
for _ in range(n):
    trie.insert(input().rstrip())
    
for _ in range(m):
    print(trie.search(input().rstrip()))
    