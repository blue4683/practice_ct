# BAEKJOON ONLINE JUDGE - 2631. 줄세우기

- [문제출처](https://www.acmicpc.net/problem/2631 '2631. 줄세우기')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if children[i] > children[j]:
            dp[i] = max(dp[i], dp[j] + 1)
```

### 설계

- 전체 `n`에서 가장 긴 증가하는 수열의 길이를 뺀 값이 최소 옮기는 횟수
