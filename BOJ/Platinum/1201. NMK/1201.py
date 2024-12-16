import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

if n < m + k - 1 or n > m * k:
    print(-1)

else:
    if k == 1:
        print(*[i for i in range(1, m + 1)])

    else:
        sizes = [1] * m
        q = (n - m) // (k - 1)
        r = (n - m) % (k - 1)
        for i in range(q):
            sizes[i] = k

        if r:
            sizes[q] += r

        result = []
        start = 0
        for size in sizes:
            for i in range(start + size, start, -1):
                result.append(i)

            start += size

        print(*result)
