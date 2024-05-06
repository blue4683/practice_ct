import sys
input = sys.stdin.readline


class Trie:
    def __init__(self):
        self.root = dict()

    def insert(self, food):
        cur = self.root

        for f in food:
            if f not in cur:
                cur[f] = dict()

            cur = cur[f]

        cur[0] = True

    def search(self, depth, cur):
        if 0 in cur:
            return

        child = sorted(cur)
        for food in child:
            print('--' * depth + food)
            self.search(depth + 1, cur[food])


n = int(input())
trie = Trie()

for i in range(n):
    _, *food = input().split()
    trie.insert(food)

trie.search(0, trie.root)
