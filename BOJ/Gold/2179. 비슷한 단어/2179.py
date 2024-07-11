import sys
input = sys.stdin.readline

n = int(input())
words = [input().rstrip() for _ in range(n)]
sorted_words = sorted(list(enumerate(words)), key=lambda x: x[1])
table = [0] * n
max_length = 0

for i in range(1, n):
    idx, word = sorted_words[i - 1]
    next_idx, next_word = sorted_words[i]
    if word == next_word:
        continue

    prefix_length = 0
    for j in range(min(len(word), len(next_word))):
        if word[j] != next_word[j]:
            break

        prefix_length += 1

    max_length = max(max_length, prefix_length)
    table[idx] = max(table[idx], prefix_length)
    table[next_idx] = max(table[next_idx], prefix_length)

s = 0
for i in range(n):
    if not s:
        if table[i] == max_length:
            s = words[i]
            prefix = s[:max_length]

    else:
        if table[i] == max_length and prefix == words[i][:max_length]:
            t = words[i]
            break

print(s)
print(t)
