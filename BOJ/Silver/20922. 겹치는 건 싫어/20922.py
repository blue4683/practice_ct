import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))

arr = [0] * 200001
left, right = 0, 1
arr[nums[0]] += 1
result = 1

cnt = 1
while left < n:
    if right < n:
        arr[nums[right]] += 1
        cnt += 1

        if arr[nums[right]] > k:
            while nums[left] != nums[right]:
                arr[nums[left]] -= 1
                cnt -= 1
                left += 1

            arr[nums[left]] -= 1
            cnt -= 1
            left += 1

        right += 1

    else:
        arr[nums[left]] -= 1
        cnt -= 1
        left += 1

    result = max(result, cnt)

print(result)
