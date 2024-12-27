from collections import deque
import sys
input = sys.stdin.readline


def is_discontinuous(arr):
    r = []
    for i in range(n):
        a = arr[i]
        b = arr[i + 1] if i != n - 1 else arr[0]
        if b - a == 1 or (a, b) == (n, 1):
            continue

        r += [i, i + 1]

    return r


def solve():
    arr = deque(lock[:])
    for i in range(1, n):
        arr.appendleft(arr.pop())
        shifted = list(arr)
        r = is_discontinuous(shifted)
        if not r:
            continue

        s, e = r[1], r[-2]
        flipped = shifted[:s] + shifted[s:e + 1][::-1] + shifted[e + 1:]
        if is_discontinuous(flipped):
            continue

        q = deque(flipped)
        for j in range(1, n):
            q.appendleft(q.pop())
            if q == result:
                print(j)
                print(s + 1, e + 1)
                print(i)
                return


def init():
    n = int(input())
    lock = list(map(int, input().split()))
    result = deque([i for i in range(1, n + 1)])

    return n, lock, result


n, lock, result = init()
solve()
