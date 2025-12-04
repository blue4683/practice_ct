import sys
input = sys.stdin.readline


n1, n2 = map(int, input().split())
ants1, ants2 = list(input().rstrip()), list(input().rstrip())
t = int(input())

group1, group2 = set(ants1), set(ants2)
for _ in range(t):
    i1, i2 = 0, 0
    if ants1[0] in group1 and ants2[0] in group2:
        ants1[0], ants2[0] = ants2[0], ants1[0]
        i1 += 1
        i2 += 1

    while i1 < n1 - 1:
        if ants1[i1] in group2 and ants1[i1 + 1] in group1:
            ants1[i1], ants1[i1 + 1] = ants1[i1 + 1], ants1[i1]
            i1 += 1

        i1 += 1

    while i2 < n2 - 1:
        if ants2[i2] in group1 and ants2[i2 + 1] in group2:
            ants2[i2], ants2[i2 + 1] = ants2[i2 + 1], ants2[i2]
            i2 += 1

        i2 += 1

print(''.join(ants1[::-1]) + ''.join(ants2))
