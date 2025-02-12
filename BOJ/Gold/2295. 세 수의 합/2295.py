import sys
input = sys.stdin.readline


def get_result():
    for i in range(n - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if arr[i] - arr[j] in numbers:
                return arr[i]

    return 0


n = int(input())
arr = sorted([int(input()) for _ in range(n)])

numbers = set()
for i in range(n):
    for j in range(i, n):
        numbers.add(arr[i] + arr[j])

print(get_result())
