n, q = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [0] * (n + 1)
for i in range(n):
    prefix[i] = prefix[i - 1] + arr[i]

for _ in range(q):
    l, r = map(int, input().split())
    print(prefix[r - 1] - prefix[l - 2])
