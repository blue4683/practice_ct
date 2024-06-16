import sys
input = sys.stdin.readline


def dfs(string):
    global result
    if len(string) == len(s):
        if string == s:
            result = 1

        return

    if string[-1] == 'A':
        dfs(string[:-1])

    if string[0] == 'B':
        dfs(string[::-1][:-1])


s = input().rstrip()
t = input().rstrip()

result = 0
dfs(t)
print(result)
