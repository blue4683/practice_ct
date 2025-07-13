import sys
input = sys.stdin.readline
MAX = (2 * (10 ** 6)) + 1

arr = [1] * MAX
arr[1] = 0
for i in range(2, MAX):
    if not arr[i]:
        continue

    for j in range(2 * i, MAX, i):
        arr[j] = 0

prime = [i for i in range(2, MAX) if arr[i]]
for _ in range(int(input())):
    n = sum(map(int, input().split()))
    if n <= 3:
        print('NO')

    elif not n % 2:
        print('YES')

    else:
        n -= 2
        for p in prime:
            if p * p > n:
                print('YES')
                break

            if not n % p:
                print('NO')
                break

        else:
            print('YES')
