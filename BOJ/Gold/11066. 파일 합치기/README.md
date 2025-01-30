# BAEKJOON ONLINE JUDGE - 11066. 파일 합치기

- [문제출처](https://www.acmicpc.net/problem/11066 '11066. 파일 합치기')
- [참고](https://growth-coder.tistory.com/131)

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 접근

- `DP`

### 점화식

```python

prefix_sum = [0] * (k + 1)
for i in range(1, k + 1):
    prefix_sum[i] = files[i - 1] + prefix_sum[i - 1]

dp = [[INF] * k for _ in range(k)]
for i in range(k):
    dp[i][i] = 0

for i in range(2, k + 1):
    for j in range(k - i + 1):
        for l in range(j, j + i - 1):
            dp[j][j + i - 1] = min(dp[j][j + i - 1], dp[j][l] + dp[l + 1]
                                    [j + i - 1] + prefix_sum[j + i] - prefix_sum[j])

```

### 설계

- 파일들의 누적합을 저장한 배열을 생성
- `i ~ j`까지 합하는데 필요한 최소 비용은 `i ~ j 구간을 두 조각으로 잘라 각각 합치는 최소 비용 + i ~ j의 누적합`과 같음
