import sys
input = sys.stdin.readline


class Node:
    def __init__(self, is_end=0):
        self.is_end = is_end
        self.children = dict()


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, string):
        cur = self.head
        for char in string:
            if cur.children.get(char) is None:
                cur.children[char] = Node()

            cur = cur.children[char]

        cur.is_end = 1

    def search(self, string):
        cur = self.head
        for char in string:
            if cur.children.get(char) is None:
                return 0

            cur = cur.children[char]

        return 1


n, m = map(int, input().split())
trie = Trie()
for word in [input().rstrip() for _ in range(n)]:
    trie.insert(word)

result = 0
for word in [input().rstrip() for _ in range(m)]:
    result += trie.search(word)

print(result)
