import sys
input = sys.stdin.readline


class Node:
    def __init__(self, is_end=0):
        self.is_end = is_end
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, user):
        nickname = ''
        cur = self.head
        for i in range(len(user)):
            char = user[i]
            if cur.children.get(char) is None:
                cur.children[char] = Node()
                if nickname == '':
                    nickname = user[:i + 1]

            cur = cur.children[char]

        cur.is_end += 1
        if nickname == '':
            nickname = user
            if cur.is_end > 1:
                nickname += str(cur.is_end)

        return nickname


n = int(input())
trie = Trie()
for _ in range(n):
    user = input().rstrip()
    print(trie.insert(user))
