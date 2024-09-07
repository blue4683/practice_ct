import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nations = []
for _ in range(n):
    nation, g, s, b = map(int, input().split())
    nations.append((g, s, b, nation))

nations.sort(reverse=True)
rank = 0

for i in range(n):
    if not i or i and nations[i][:-1] != nations[i - 1][:-1]:
        rank = i + 1

    if nations[i][-1] == k:
        break

print(rank)
