import sys
input = sys.stdin.readline

n, m = map(int, input().split())
keywords = set(input().rstrip() for _ in range(n))

for _ in range(m):
    post = set(input().rstrip().split(','))
    keywords -= post
    print(len(keywords))
