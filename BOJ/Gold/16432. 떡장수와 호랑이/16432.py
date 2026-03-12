import sys
input = sys.stdin.readline


n = int(input())
arr = [[]]
for _ in range(n):
    m, *l = map(int, input().split())
    arr.append(l)

dp = [[0] * 10 for _ in range(n + 1)]
prev = [[0] * 10 for _ in range(n + 1)]

for item in arr[1]:
    dp[1][item] = 1

for day in range(2, n + 1):
    for item in arr[day]:
        for k in range(1, 10):
            if k != item and dp[day - 1][k]:
                dp[day][item] = 1
                prev[day][item] = k
                break

last = -1
for item in range(1, 10):
    if dp[n][item]:
        last = item
        break

if last == -1:
    print(-1)

else:
    result = [0] * (n + 1)
    cur = last
    for day in range(n, 0, -1):
        result[day] = cur
        cur = prev[day][cur]

    for i in range(1, n + 1):
        print(result[i])
