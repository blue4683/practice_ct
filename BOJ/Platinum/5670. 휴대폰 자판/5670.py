import sys
input = sys.stdin.readline


class Node:
    def __init__(self, is_end=False):
        self.is_end = is_end
        self.children = dict()
        self.cnt = 0


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, string):
        cur = self.head

        for char in string:
            if cur.children.get(char) is None:
                cur.children[char] = Node()
                cur.cnt += 1

            cur = cur.children[char]

        cur.is_end = True

    def search(self, string):
        cur = self.head
        cnt = 1

        for i in range(len(string)):
            char = string[i]
            if (i != 0 and (cur.cnt != 1 or (cur.cnt == 1 and cur.is_end))) and cur.children.get(char) is not None:
                cnt += 1

            cur = cur.children[char]

        return cnt


while 1:
    try:
        n = int(input())
    except:
        break

    words = [input().rstrip() for _ in range(n)]
    words.sort(key=lambda x: len(x))
    trie = Trie()

    for word in words:
        trie.insert(word)

    result = sum(trie.search(word) for word in words)
    print(f'{result / n:.2f}')
