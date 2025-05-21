import sys
input = sys.stdin.readline


n = int(input())
logs = set()
for _ in range(n):
    name, enter = input().split()
    if enter == 'leave' and name in logs:
        logs.remove(name)

    else:
        logs.add(name)

for name in sorted(logs, reverse=True):
    print(name)
