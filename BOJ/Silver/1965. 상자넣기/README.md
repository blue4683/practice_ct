# BAEKJOON ONLINE JUDGE - 1965. 상자넣기

- [문제출처](https://www.acmicpc.net/problem/1965 '1965. 상자넣기')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] < arr[j]:
            dp[j] = max(dp[j], dp[i] + 1)

```

### 설계

- 뒤에 수가 앞에 수보다 큰 경우 dp배열 업데이트
