import sys
input = sys.stdin.readline


def dfs(idx, seq, used):
    if idx == len(word):
        tmp = sorted(seq)
        if tmp == [i for i in range(1, tmp[-1] + 1)]:
            print(*seq)
            exit()

        return

    if int(word[idx]) not in used:
        dfs(idx + 1, seq + [int(word[idx])], used | {int(word[idx])})

    if idx + 2 <= len(word) and int(word[idx:idx + 2]) <= n and int(word[idx:idx + 2]) not in used:
        dfs(idx + 2, seq + [int(word[idx:idx + 2])],
            used | {int(word[idx:idx + 2])})


word = input().rstrip()
if len(word) < 10:
    n = len(word)

else:
    n = (len(word) - 9) // 2 + 9

dfs(0, [], set())
