import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

result = [arr[0]]
index_list = [(arr[0], 0)]
for i in range(1, n):
    if result[-1] < arr[i]:
        result.append(arr[i])
        index_list.append((arr[i], len(result) - 1))

    else:
        l, r = 0, len(result) - 1
        while l < r:
            mid = (l + r) // 2
            if result[mid] < arr[i]:
                l = mid + 1

            else:
                r = mid

        result[r] = arr[i]
        index_list.append((arr[i], r))

print(len(result))

idx = len(result) - 1
nums = []
for i in range(len(index_list) - 1, -1, -1):
    if index_list[i][1] == idx:
        nums.append(index_list[i][0])
        idx -= 1

print(*nums[::-1])
