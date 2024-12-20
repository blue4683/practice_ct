import sys
input = sys.stdin.readline

n = int(input())
mlt, mmt = [], []
wlt, wmt = [], []

for man in map(int, input().split()):
    if man < 0:
        mlt.append(-man)

    else:
        mmt.append(man)

for woman in map(int, input().split()):
    if woman < 0:
        wlt.append(-woman)

    else:
        wmt.append(woman)

mlt.sort(reverse=True)
mmt.sort(reverse=True)
wlt.sort(reverse=True)
wmt.sort(reverse=True)

result = 0

l, r = 0, 0
mn, wn = len(mlt), len(wmt)
while l < mn and r < wn:
    if mlt[l] > wmt[r]:
        result += 1
        l += 1

    r += 1

l, r = 0, 0
mn, wn = len(mmt), len(wlt)
while l < mn and r < wn:
    if mmt[l] < wlt[r]:
        result += 1
        r += 1

    l += 1

print(result)
