import sys
input = sys.stdin.readline

a, b = map(int, input().split())
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

result_a = set_a - set_b
if result_a:
    print(len(result_a))
    print(*sorted(result_a))

else:
    print(0)
