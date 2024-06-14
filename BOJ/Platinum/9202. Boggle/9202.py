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

        for i in range(len(string)):
            char = string[i]
            if cur.children.get(char) is None:
                return 0

            cur = cur.children[char]

        return cur.is_end


def dfs(y, x, word):
    global result, longest_word, word_cnt
    if len(word) == 9:
        return

    if trie.search(word):
        if word not in duplication:
            duplication.add(word)
            word_cnt += 1
            result += score[len(word)]
            if len(longest_word) < len(word):
                longest_word = word

            elif len(longest_word) == len(word):
                longest_word = sorted([longest_word, word])[0]

    for dy, dx in d:
        yy, xx = y + dy, x + dx
        if 0 <= yy < 4 and 0 <= xx < 4 and not visited[yy][xx]:
            visited[yy][xx] = 1
            dfs(yy, xx, word + boggle[yy][xx])
            visited[yy][xx] = 0


d = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
score = [0, 0, 0, 1, 1, 2, 3, 5, 11]

n = int(input())
trie = Trie()
for _ in range(n):
    trie.insert(input().rstrip())

input()
b = int(input())
for i in range(b):
    boggle = [list(input().rstrip()) for _ in range(4)]
    visited = [[0] * 4 for _ in range(4)]
    duplication = set()
    result = 0
    longest_word = ''
    word_cnt = 0

    for y in range(4):
        for x in range(4):
            visited[y][x] = 1
            dfs(y, x, boggle[y][x])
            visited[y][x] = 0

    print(*[result, longest_word, word_cnt])
    if i != b - 1:
        input()
