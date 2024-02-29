import sys
input = sys.stdin.readline


def reverse_coins(coin):
    for i in range(len(coin)):
        coin[i] ^= 1

    return coin


def count_tail(coins):
    cnt = 0
    for x in range(n):
        tmp = 0
        for y in range(n):
            if not coins[y][x]:
                tmp += 1
        cnt += min(tmp, n - tmp)

    return cnt


n = int(input())
coins = [list(input().rstrip()) for _ in range(n)]
result = 400

for bit in range(1 << n):
    tmp = [list(map(lambda x: 1 if x == 'H' else 0, coins[y]))
           for y in range(n)]
    for i in range(n):
        if bit & (1 << i) != 0:
            tmp[i] = reverse_coins(tmp[i])

    tail = count_tail(tmp)
    result = min(result, tail)

print(result)
