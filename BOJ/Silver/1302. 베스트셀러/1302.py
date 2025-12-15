from collections import defaultdict
import sys
input = sys.stdin.readline


n = int(input())
books = defaultdict(int)
for _ in range(n):
    books[input().rstrip()] += 1

print(sorted(books.items(), key=lambda x: (-x[1], x[0]))[0][0])
