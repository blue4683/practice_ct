from collections import Counter
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
words = [input().rstrip() for _ in range(n)]
counter = Counter(words)
count = counter.most_common()
count.sort()
count.sort(key=lambda x: len(x[0]), reverse=True)
count.sort(key=lambda x: x[1], reverse=True)

for word, cnt in count:
    if len(word) >= m:
        print(word)
