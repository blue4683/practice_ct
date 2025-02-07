import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

psum = arr[0]
left, right = 0, 0

result = 0
while left < n:
    if psum <= m:
        if psum == m:
            result += 1

        if right < n - 1:
            right += 1
            psum += arr[right]

        else:
            break

    else:
        psum -= arr[left]
        left += 1

print(result)
