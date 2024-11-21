import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
judges = list(map(int, input().split()))
start, end = 0, judges[-1] + 1

while start + 1 < end:
    mid = (start + end) // 2
    now = -1
    cnt = 0
    for i in range(k):
        if now <= judges[i]:
            cnt += 1
            now = judges[i] + mid

    if cnt >= m:
        start = mid

    else:
        end = mid

result = ''
now = 0
cnt = 0
for i in range(k):
    if now <= judges[i] and cnt < m:
        result += '1'
        now = judges[i] + start
        cnt += 1

    else:
        result += '0'

print(result)
