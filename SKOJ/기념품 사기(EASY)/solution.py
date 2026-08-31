from bisect import bisect_left


n, q = map(int, input().split())
arr = sorted(map(int, input().split()))
for _ in range(q):
    a, x = map(int, input().split())
    if a == 1:
        arr.append(x)
        arr.sort()

    elif a == 2:
        i = bisect_left(arr, x)
        arr.pop(i)

    else:
        j = bisect_left(arr, x)
        if j < len(arr) and arr[j] == x:
            print(x)
            continue

        i = j - 1
        vl = vr = float('inf')
        if i >= 0:
            vl = x - arr[i]

        if j < len(arr):
            vr = arr[j] - x

        print(arr[i] if vl <= vr else arr[j])
