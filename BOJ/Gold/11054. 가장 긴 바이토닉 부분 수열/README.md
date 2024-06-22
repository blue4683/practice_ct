# BAEKJOON ONLINE JUDGE - 11054. 가장 긴 바이토닉 부분 수열

- [문제출처](https://www.acmicpc.net/problem/11054 '11054. 가장 긴 바이토닉 부분 수열')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            increase_dp[i] = max(increase_dp[i], increase_dp[j] + 1)

        if reversed_arr[i] > reversed_arr[j]:
            decrease_dp[i] = max(decrease_dp[i], decrease_dp[j] + 1)

```

### 설계

- 입력 배열의 `reverse` 배열 생성
- 가장 긴 증가하는 부분 수열과 가장 긴 감소하는 부분 수열 `dp` 테이블 생성
- `increase_dp[i] + decrease_dp[n - i - 1] - 1` 값이 가장 큰 값을 출력
