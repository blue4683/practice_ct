import sys
input = sys.stdin.readline


for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    result = [0]
    for i in range(n):
        if result[-1] < arr[i]:
            result.append(arr[i])

        else:
            l, r = 0, len(result) - 1
            while l < r:
                m = (l + r) // 2
                if result[m] < arr[i]:
                    l = m + 1

                else:
                    r = m

            result[r] = arr[i]

    print(f'Case #{tc}')
    print(int(len(result) - 1 >= k))
