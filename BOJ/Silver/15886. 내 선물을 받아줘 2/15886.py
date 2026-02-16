import sys
input = sys.stdin.readline


n = int(input())
arr = input().rstrip()

result = 0
visited = [0] * n
for x in range(n):
    if visited[x]:
        continue

    new = 1
    now = {x}
    while 1:
        dx = 1 if arr[x] == 'E' else -1
        xx = x + dx
        if xx in now:
            break

        if visited[xx]:
            new = 0
            break

        now.add(xx)
        x = xx

    result += new
    for xx in now:
        visited[xx] = 1

print(result)
