from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
counter = Counter(arr)
print(sorted(counter.most_common(), key=lambda x: (-x[1], x[0]))[0][0])
