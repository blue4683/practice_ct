import sys
input = sys.stdin.readline
num_list = [0]*10001
n = int(input())
for _ in range(n):
    num_list[int(input())] += 1

for idx in range(1, len(num_list)):
    for _ in range(num_list[idx]):
        print(idx)