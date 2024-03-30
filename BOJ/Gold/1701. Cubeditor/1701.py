import sys
input = sys.stdin.readline

word = input().rstrip()
n = len(word)
result = 0

for i in range(n):
    pattern = word[i:]
    m = len(pattern)
    table = [0] * m
    j = 0

    for k in range(1, m):
        while j > 0 and pattern[k] != pattern[j]:
            j = table[j - 1]

        if pattern[k] == pattern[j]:
            j += 1
            table[k] = j

    result = max(result, max(table))

print(result)
