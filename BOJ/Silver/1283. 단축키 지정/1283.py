import sys
input = sys.stdin.readline


def select(word):
    arr = word.split()
    for i in range(len(arr)):
        alp = arr[i]
        if alp[0].lower() not in hotkeys:
            hotkeys.add(alp[0].lower())
            arr[i] = f'[{alp[0]}]' + alp[1:]
            return ' '.join(arr)

    for i in range(len(word)):
        if word[i] != ' ' and word[i].lower() not in hotkeys:
            hotkeys.add(word[i].lower())
            return word[:i] + f'[{word[i]}]' + word[i + 1:]

    return word


n = int(input())
hotkeys = set()
words = [input().rstrip() for _ in range(n)]
for word in words:
    print(select(word))
