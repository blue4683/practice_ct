import sys
input = sys.stdin.readline


def get_gcd(a, b):
    if not b:
        return a

    return get_gcd(b, a % b)


for _ in range(int(input())):
    n, *arr = map(int, input().split())
    result = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            result += get_gcd(arr[i], arr[j])

    print(result)
