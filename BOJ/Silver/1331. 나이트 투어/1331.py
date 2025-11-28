import sys
input = sys.stdin.readline

arr = [input().rstrip() for _ in range(36)]
start = arr[0]
visited = {start}
result = 'Valid'
for i in range(1, 36):
    if arr[i] in visited or abs((ord(arr[i - 1][0]) - ord(arr[i][0])) * (int(arr[i - 1][1]) - int(arr[i][1]))) != 2:
        result = 'Invalid'
        break

    visited.add(arr[i])

else:
    if abs((ord(arr[i][0]) - ord(start[0])) * (int(arr[i][1]) - int(start[1]))) != 2:
        result = 'Invalid'

print(result)
