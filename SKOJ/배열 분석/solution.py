n = int(input())
arr = list(map(int, input().split()))
sorted_arr = sorted(arr)
l, r = sorted_arr[0], sorted_arr[-1]
print(l, arr.index(l) + 1)
print(r, arr.index(r) + 1)
