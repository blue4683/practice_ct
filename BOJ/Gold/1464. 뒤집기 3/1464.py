import sys
input = sys.stdin.readline


s = input().rstrip()
n = len(s)
for i in range(n - 1):
    if s[i] >= s[i + 1]:
        continue

    s = s[:i + 1][::-1] + s[i + 1:]
    s = s[:i + 2][::-1] + s[i + 2:]

print(s[::-1])
