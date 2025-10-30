from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(folder):
    file_list = files[folder][:]
    for f in folders[folder]:
        file = dfs(f)
        file_list += file

    return file_list


n, m = map(int, input().split())
files, folders = defaultdict(list), defaultdict(list)
for _ in range(n + m):
    p, f, c = list(input().split())
    if c == '1':
        folders[p].append(f)

    else:
        files[p].append(f)

for _ in range(int(input())):
    query = input().rstrip().split('/')
    file = dfs(query[-1])
    print(len(set(file)), len(file))
