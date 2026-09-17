n = int(input())
arr = list(map(int, input().split()))
print(n - len(set(arr)) + 1)
