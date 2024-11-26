import sys
input = sys.stdin.readline

arr = input().rstrip()
target = input().rstrip()
result = []

arr_cnt = [0] * 10
target_cnt = [0] * 10

for i in arr:
    arr_cnt[int(i)] += 1

for i in target:
    target_cnt[int(i)] += 1

for i in arr:
    i = int(i)
    if target_cnt[i] and arr_cnt[i] == target_cnt[i]:
        arr_cnt[i] -= 1
        target_cnt[i] -= 1

    else:
        while result:
            if result[-1] >= i or not target_cnt[result[-1]]:
                break

            target_cnt[result[-1]] -= 1
            result.pop()

        arr_cnt[i] -= 1
        result.append(i)

print(''.join(map(str, result)))
