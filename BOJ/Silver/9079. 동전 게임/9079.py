import sys
input = sys.stdin.readline
INF = 10 ** 9
lines = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],

    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],

    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]


def flip(line):
    for y, x in line:
        tmp[y][x] ^= 1


for _ in range(int(input())):
    arr = []
    for _ in range(3):
        coins = list(map(lambda x: 1 if x == 'H' else 0, input().split()))
        arr.append(coins)

    result = INF
    for bit in range(1 << 8):
        tmp = [l[:] for l in arr]
        cnt = 0
        for i in range(8):
            if bit & (1 << i):
                flip(lines[i])
                cnt += 1

        if sum(map(sum, tmp)) in [0, 9]:
            result = min(result, cnt)

    print(result if result != INF else -1)
