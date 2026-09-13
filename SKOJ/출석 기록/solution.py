n = int(input())
arr = [input().rstrip() for _ in range(n)]
unique_name = set(arr)
print(len(unique_name), n - len(unique_name))
