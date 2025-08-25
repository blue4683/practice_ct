# BAEKJOON ONLINE JUDGE - 2515. 전시장

- [문제출처](https://www.acmicpc.net/problem/2515 '2515. 전시장')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 정렬
- 이분 탐색

## 풀이

### 접근

- `DP`

### 점화식

```python

dp = [0] * (2 * (10 ** 7) + 1)
for i in range(s + 1):
    dp[i] = arr[i]

for i in range(s + 1, max_h + 1):
    dp[i] = dp[i - 1]
    dp[i] = max(dp[i], dp[i - s] + arr[i])

```

### 설계

- 그림의 높이에 따라 최고 가격을 리스트에 저장
- 그림의 높이를 기준으로 배치할 수 있는 경우를 dp 배열에 저장하며 탐색
