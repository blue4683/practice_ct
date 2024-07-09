import sys
input = sys.stdin.readline


def check():
    result = ''
    i = 0
    while i < k:
        if player[i] == order[i]:
            result += '*'
            i += 1
            continue

        else:
            if i == k - 1:
                return 0

            elif player[i] == order[i + 1] and order[i] == player[i + 1]:
                result += '-*'
                i += 2

            else:
                return 0

    return result


k = int(input())
n = int(input())
player = [chr(ord('A') + i) for i in range(k)]
order = list(input().rstrip())
ladder = [list(input().rstrip()) for _ in range(n)]
h = [y for y in range(n) if ladder[y][0] == '?'][0]

for y in range(h):
    for x in range(k - 1):
        if ladder[y][x] == '-':
            player[x], player[x + 1] = player[x + 1], player[x]

for y in range(n - 1, h, -1):
    for x in range(k - 1):
        if ladder[y][x] == '-':
            order[x], order[x + 1] = order[x + 1], order[x]

result = check()
print(result[:k - 1]) if result else print('x' * (k - 1))
