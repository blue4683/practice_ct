import sys
input = sys.stdin.readline


class Node:
    def __init__(self, is_end=0):
        self.is_end = is_end
        self.children = dict()


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, directory):
        cur = self.head
        for file in directory:
            if cur.children.get(file) is None:
                cur.children[file] = Node()

            cur = cur.children[file]

        cur.is_end = 1

    def search(self, depth, cur):
        for key in sorted(cur.children.keys()):
            print(' ' * depth + key)
            self.search(depth + 1, cur.children[key])


n = int(input())
files = Trie()
for _ in range(n):
    directory = input().rstrip().split('\\')
    files.insert(directory)

files.search(0, files.head)
