import sys
input = sys.stdin.readline


def get_sum(arr, left, right):
    if left <= right:
        return sum(arr[left:right])

    return sum(arr[left:]) + sum(arr[:right])


size = int(input())
m, n = map(int, input().split())
pieces1 = [int(input()) for _ in range(m)]
pieces2 = [int(input()) for _ in range(n)]

suffix1, suffix2 = [0] * (size + 1), [0] * (size + 1)

suffix1[0] = 1
suffix2[0] = 1

for left in range(m):
    for right in range(left + 1, m + 1):
        suffix = get_sum(pieces1, left, right)
        if suffix > size:
            break

        suffix1[suffix] += 1

    for right in range(1, left):
        suffix = get_sum(pieces1, left, right)
        if suffix > size:
            break

        suffix1[suffix] += 1

for left in range(n):
    for right in range(left + 1, n + 1):
        suffix = get_sum(pieces2, left, right)
        if suffix > size:
            break

        suffix2[suffix] += 1

    for right in range(1, left):
        suffix = get_sum(pieces2, left, right)
        if suffix > size:
            break

        suffix2[suffix] += 1

result = 0
for piece in range(size + 1):
    result += suffix1[piece] * suffix2[size - piece]

print(result)
