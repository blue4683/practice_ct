import sys
input = sys.stdin.readline

leds = [0b1110111, 0b0100100, 0b1011101, 0b1101101, 0b0101110,
        0b1101011, 0b1111011, 0b0100101, 0b1111111, 0b1101111]

n, k, p, x = map(int, input().split())
number = list(map(lambda x: leds[int(x)], str(x).zfill(k + 1)))
result = 0
for level in range(1, n + 1):
    if level == x:
        continue

    level = list(map(lambda x: leds[int(x)], str(level).zfill(k + 1)))
    reversal = 0
    for i in range(k, -1, -1):
        bit = level[i] ^ number[i]
        for j in range(7):
            if not (bit & 1 << j):
                continue

            reversal += 1

        if reversal > p:
            break

    else:
        result += 1

print(result)
