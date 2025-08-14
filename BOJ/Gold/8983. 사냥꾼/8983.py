import sys
input = sys.stdin.readline

m, n, l = map(int, input().split())
pos = sorted(map(int, input().split()))
animals = [list(map(int, input().split())) for _ in range(n)]

result = 0
for x, y in animals:
    s, e = 0, m - 1
    while s <= e:
        mid = (s + e) // 2
        if x >= pos[mid]:
            s = mid + 1

        elif x < pos[mid]:
            e = mid - 1

    if abs(x - pos[s % m]) + y <= l or abs(x - pos[s - 1]) + y <= l:
        result += 1

print(result)
