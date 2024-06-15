import sys
input = sys.stdin.readline


def dfs(string, is_right, index):
    if len(string) <= 0:
        return

    char = min(string)
    char_idx = string.index(char)
    if is_right:
        index += 1

    result.insert(index, char)

    print(''.join(result))
    dfs(string[char_idx + 1:], 1, index)
    dfs(string[:char_idx], 0, index)


word = list(input().rstrip())
n = len(word)
result = []
dfs(word, 0, 0)
