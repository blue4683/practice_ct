import sys
input = sys.stdin.readline

t = '0' + input().rstrip()
pattern = input().rstrip()
n, m = map(lambda x: len(x), [t, pattern])

table = [0] * m
i = 0
for j in range(1, m):
    while i > 0 and pattern[i] != pattern[j]:
        i = table[i - 1]

    if pattern[i] == pattern[j]:
        i += 1
        table[j] = i

result = []
i = 0
for j in range(n):
    while i > 0 and pattern[i] != t[j]:
        i = table[i - 1]

    if pattern[i] == t[j]:
        i += 1

        if i == m:
            result.append(j - i + 1)
            i = table[i - 1]

print(len(result))
print(*result)
