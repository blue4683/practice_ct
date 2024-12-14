import sys
input = sys.stdin.readline

n, s, r = map(int, input().split())
damaged = set(map(int, input().split()))
more = set(map(int, input().split()))

remain = set()
for team in more:
    if team in damaged:
        damaged.discard(team)

    else:
        remain.add(team)

for team in remain:
    if team - 1 in damaged:
        damaged.discard(team - 1)

    elif team + 1 in damaged:
        damaged.discard(team + 1)

print(len(damaged))
