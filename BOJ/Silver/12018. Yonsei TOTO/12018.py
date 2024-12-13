import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mileages = []
for _ in range(n):
    p, l = map(int, input().split())
    mileage = sorted(map(int, input().split()), reverse=True)
    if len(mileage) >= l:
        mileages.append(mileage[l - 1])

    else:
        mileages.append(1)

mileages.sort()
result = 0
for mileage in mileages:
    if m < mileage:
        break

    result += 1
    m -= mileage

print(result)
