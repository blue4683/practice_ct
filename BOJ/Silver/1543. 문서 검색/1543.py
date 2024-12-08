import sys
input = sys.stdin.readline

word = input().rstrip()
pattern = input().rstrip()

n, m = map(len, [word, pattern])
result = 0

s = 0
while s < n - m + 1:
    if word[s: s + m] == pattern:
        result += 1
        s = s + m

    else:
        s += 1

print(result)
