import sys
input = sys.stdin.readline


def str_to_num(s):
    if ord(s) >= ord('a'):
        return ord(s) - ord('a') + 26

    return ord(s) - ord('A')


g, s = map(int, input().split())
word, string = [input().rstrip() for _ in range(2)]
table = [0] * 52
for w in word:
    table[str_to_num(w)] += 1

visited = [0] * 52
for i in range(g):
    visited[str_to_num(string[i])] += 1

result = 1 if table == visited else 0
for i in range(g, s):
    visited[str_to_num(string[i])] += 1
    visited[str_to_num(string[i - g])] -= 1
    if table != visited:
        continue

    result += 1

print(result)
