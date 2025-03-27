import sys
input = sys.stdin.readline


def find(x, y):
    result = 0
    while 1:
        if x == y:
            return result

        elif x > y:
            result += 1
            x = (x + k - 2) // k

        else:
            result += 1
            y = (y + k - 2) // k


n, k, q = map(int, input().split())
for _ in range(q):
    x, y = map(int, input().split())
    if k == 1:
        print(abs(x - y))

    else:
        print(find(x, y))
