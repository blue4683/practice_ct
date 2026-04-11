import sys
input = sys.stdin.readline

s = list(input().rstrip())
alps = set(s)
d = {}
for _ in range(int(input())):
    alp, l, r = input().split()
    if alp not in alps:
        print(0)
        continue

    l, r = int(l), int(r)
    if alp not in d.keys():
        d[alp] = list(map(lambda x: int(x == alp), s))
        for i in range(len(s) - 1):
            d[alp][i + 1] += d[alp][i]

    print(d[alp][r] - d[alp][l - 1]) if l else print(d[alp][r])
