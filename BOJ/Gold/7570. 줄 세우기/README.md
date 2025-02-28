# BAEKJOON ONLINE JUDGE - 7570. 줄 세우기

- [문제출처](https://www.acmicpc.net/problem/7570 '7570. 줄 세우기')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 그리디 알고리즘

## 풀이

### 접근

- `DP`

### 점화식

```python

dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[arr[i]] = i

num = 1
result = 1
for i in range(1, n):
    if dp[i] < dp[i + 1]:
        num += 1
        result = max(result, num)

    else:
        num = 1

```

### 설계

- 1씩 증가하는 최장부분수열의 길이를 구한 뒤 `n`에서 빼줌
