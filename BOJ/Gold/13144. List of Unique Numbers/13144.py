import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
visited = [0] * 100001
result = 0

start, end = 0, 0
visited[nums[0]] = 1
while 1:
    if end < n - 1:
        if visited[nums[end + 1]]:
            if start == end:
                result += 1
                start += 1
                end += 1

            else:
                result += end - start + 1
                visited[nums[start]] = 0
                start += 1

        else:
            end += 1
            visited[nums[end]] = 1

    else:
        if start < n:
            result += end - start + 1
            start += 1

        else:
            break

print(result)
