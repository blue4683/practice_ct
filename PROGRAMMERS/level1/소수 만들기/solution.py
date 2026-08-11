from itertools import combinations


def solution(nums):
    answer = 0
    combs = list(map(sum, combinations(nums, 3)))
    n = max(combs)
    arr = [1] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        for j in range(2, n // i + 1):
            arr[i * j] = 0
            
    for num in combs:
        answer += arr[num]

    return answer
