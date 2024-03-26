import sys
input = sys.stdin.readline

n, k = map(int, input().split())
elecs = list(map(int, input().split()))
holes = set()
result = 0

for i, elec in enumerate(elecs):
    holes.add(elec)
    if len(holes) > n:
        target, max_idx = 0, 0
        for hole in holes:
            hole_idx = elecs[i:].index(hole) if hole in elecs[i:] else k
            if hole_idx > max_idx:
                target, max_idx = hole, hole_idx

        holes.discard(target)
        result += 1

print(result)
