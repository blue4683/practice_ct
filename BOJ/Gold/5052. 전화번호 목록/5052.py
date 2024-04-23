import sys
input = sys.stdin.readline


class Node:
    def __init__(self, is_end=False):
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

        cur.is_end = True

    def search(self, string):
        cur = self.head

        for char in string:
            if cur.children.get(char) is None:
                return 1

            cur = cur.children[char]
            if cur.is_end:
                return 0

        return 1


for _ in range(int(input())):
    n = int(input())
    words = [input().rstrip() for _ in range(n)]
    words.sort(key=len)
    trie = Trie()
    for word in words:
        if trie.search(word) == 0:
            print('NO')
            break

        trie.insert(word)

    else:
        print('YES')
