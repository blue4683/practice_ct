n, s = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
l = 0
v = 0
for r in range(n):
    v += arr[r]
    while v > s:
        v -= arr[l]
        l += 1
    if v == s:
        result += 1

print(result)
