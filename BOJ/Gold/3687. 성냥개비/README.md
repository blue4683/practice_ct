# BAEKJOON ONLINE JUDGE - 3687. 성냥개비

- [문제출처](https://www.acmicpc.net/problem/3687 '3687. 성냥개비')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 그리디 알고리즘

## 풀이

### 접근

- `DP`

### 점화식

```python3
if i == cnt:
    if m == '0':
        continue

    if max_dp[i] == '0':
        max_dp[i] = m

    else:
        max_dp[i] = str(max(int(max_dp[i]), int(m)))

    if min_dp[i] == '9' * 50:
        min_dp[i] = m

    else:
        min_dp[i] = str(min(int(min_dp[i]), int(m)))

elif i - cnt >= 0:
    max_dp[i] = str(
        max(int(max_dp[i]), int(max_dp[i - cnt] + m)))

    min_dp[i] = str(
        min(int(min_dp[i]), int(min_dp[i - cnt] + m)))
```

### 설계

- `2 ~ n`까지 최댓값, 최솟값 테이블 갱신
  - `n == 6`일 때 `0`이 최솟값으로 사용되는 것을 막기 위해 조건 추가 (`0`은 시작으로 사용할 수 없음)
