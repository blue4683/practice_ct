import sys
input = sys.stdin.readline

s = list(map(int, list(input().rstrip())))
result = [0, 0]
for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        result[s[i - 1]] += 1

result[s[-1]] += 1
print(min(result))
