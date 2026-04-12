import sys
input = sys.stdin.readline


s = input().rstrip()
n = len(s)
d = set()
for i in range(n):
    for j in range(i, n):
        d.add(s[i:j + 1])

print(len(d))
