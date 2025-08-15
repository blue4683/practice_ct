import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
result = [arr[0]]

for i in range(1, n):
    if result[-1] < arr[i]:
        result.append(arr[i])

    else:
        l, r = 0, len(result) - 1
        while l < r:
            m = (l + r) // 2
            if result[m] < arr[i]:
                l = m + 1

            else:
                r = m

        result[r] = arr[i]

print(n - len(result))
