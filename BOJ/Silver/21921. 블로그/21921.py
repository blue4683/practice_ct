import sys
input = sys.stdin.readline

n, x = map(int, input().split())
visitors = list(map(int, input().split()))

cnt = sum(visitors[:x])
result = [cnt, 1]
for i in range(x, n):
    cnt = cnt - visitors[i - x] + visitors[i]
    if cnt > result[0]:
        result = [cnt, 1]

    elif cnt == result[0]:
        result[1] += 1

if not result[0]:
    print('SAD')

else:
    for res in result:
        print(res)
