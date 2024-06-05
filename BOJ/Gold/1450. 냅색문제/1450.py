import sys
input = sys.stdin.readline


def get_weight(left, right, weights, weight):
    if left > right:
        weights.append(weight)
        return

    get_weight(left + 1, right, weights, weight)
    get_weight(left + 1, right, weights, weight + arr[left])


def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] <= target:
            left = mid + 1

        else:
            right = mid

    return right


n, c = map(int, input().split())
arr = list(map(int, input().split()))
weights1, weights2 = [], []
result = 0

get_weight(0, n // 2, weights1, 0)
get_weight(n // 2 + 1, n - 1, weights2, 0)

weights2.sort()

for weight in weights1:
    result += upper_bound(weights2, c - weight)

print(result)
