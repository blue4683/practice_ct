# BAEKJOON ONLINE JUDGE - 9252. LCS 2

- [문제출처](https://www.acmicpc.net/problem/9252 '9252. LCS 2')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 문자열

## 풀이

### 접근

- `DP`

### 점화식

```python

dp = [[0] * (m + 1) for _ in range(n + 1)]
for y in range(1, n + 1):
    for x in range(1, m + 1):
        if a[y - 1] == b[x - 1]:
            dp[y][x] = dp[y - 1][x - 1] + 1

        else:
            dp[y][x] = max(dp[y][x - 1], dp[y - 1][x])

```

### 설계

- dp테이블을 생성해 두 문자열의 공통된 부분 수열의 길이를 저장
- dp테이블의 끝에서부터 역추적해 부분 수열에 해당하는 문자를 찾아 저장
