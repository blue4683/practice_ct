import sys
input = sys.stdin.readline


for _ in range(int(input())):
    arr = list(input().rstrip())
    if not arr:
        print(1)
        continue

    r = 0
    cnt = 0
    for x in arr:
        if x == '[':
            cnt += 1

        else:
            cnt -= 1

        r = max(r, cnt)

    result = 1
    for _ in range(r):
        result *= 2

    print(result)
