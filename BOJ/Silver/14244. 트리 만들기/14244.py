import sys
input = sys.stdin.readline


n, m = map(int, input().split())
for i in range(n - m):
    print(i, i + 1)

node = n - m
for i in range(m - 1):
    print(node, node + i + 1)
