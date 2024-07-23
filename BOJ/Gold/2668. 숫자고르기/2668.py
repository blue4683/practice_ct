import sys
input = sys.stdin.readline


def travesal(now, indexes, nums):
    global result
    next = arr[now]
    if next in indexes:
        if indexes == nums:
            if result[1] - indexes == result[1]:
                result = (result[0] + len(indexes), result[1] | indexes)

            if result[0] < len(indexes):
                result = (len(indexes), indexes)

        return

    travesal(next, indexes | {next}, nums | {arr[next]})


n = int(input())
arr = [0] + [int(input()) for _ in range(n)]
indexes = set()
for i, num in enumerate(arr):
    if not i or i != num:
        continue

    indexes.add(i)

result = (len(indexes), indexes)
for i in range(1, n + 1):
    if i not in indexes:
        travesal(i, {i}, {arr[i]})

print(result[0])
for index in sorted(result[1]):
    print(index)
