from heapq import *
import sys
input = sys.stdin.readline


class string:
    def __init__(self, word):
        self.word = word

    def __lt__(self, other):
        if self.word + other.word < other.word + self.word:
            return 1

        return 0


n = int(input())
words = []
for _ in range(n):
    heappush(words, string(input().rstrip()))

result = ''
while words:
    word = heappop(words).word
    result += word[0]
    if len(word) > 1:
        heappush(words, string(word[1:]))

print(result)
