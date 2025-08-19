import sys
input = sys.stdin.readline


def play(hp, atk):
    max_hp = hp
    for t, a, h in rooms:
        if t == 1:
            cnt = (h // atk) + ((h % atk) > 0)
            if a * (cnt - 1) >= hp:
                return 0

            hp -= a * (cnt - 1)

        else:
            atk += a
            hp = hp + h if hp + h < max_hp else max_hp

    return 1


n, atk = map(int, input().split())
rooms = [tuple(map(int, input().split())) for _ in range(n)]
l, r = 0, n * (10 ** 12)
while l < r:
    mid = (l + r) // 2
    if play(mid, atk):
        r = mid

    else:
        l = mid + 1

print(l)
