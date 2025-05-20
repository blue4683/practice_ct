import sys
input = sys.stdin.readline


n, k = map(int, input().split())
mod = [(i + 1) * 9 * (10 ** i) for i in range(10)]
num = 0
for i in range(10):
    if k - mod[i] > 0:
        num += (mod[i] // (i + 1))
        k -= mod[i]
        continue

    num += (k // (i + 1)) + (k % (i + 1) != 0)
    result = -1 if num > n else str(num)[k % (i + 1) - 1]
    break

print(result)
