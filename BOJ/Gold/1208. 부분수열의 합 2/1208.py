from collections import defaultdict
import sys
input = sys.stdin.readline


def right_subsum(mid, prefix_sum):
    if mid == n:
        subsum[prefix_sum] += 1
        return

    right_subsum(mid + 1, prefix_sum + arr[mid])
    right_subsum(mid + 1, prefix_sum)


def left_subsum(start, prefix_sum):
    global result
    if start == n // 2:
        result += subsum[s - prefix_sum]
        return

    left_subsum(start + 1, prefix_sum + arr[start])
    left_subsum(start + 1, prefix_sum)


n, s = map(int, input().split())
arr = list(map(int, input().split()))
subsum = defaultdict(int)
result = 0

right_subsum(n // 2, 0)
left_subsum(0, 0)

if not s:
    result -= 1

print(result)
