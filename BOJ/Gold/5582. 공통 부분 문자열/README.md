# BAEKJOON ONLINE JUDGE - 5582. 공통 부분 문자열

- [문제출처](https://www.acmicpc.net/problem/5582 '5582. 공통 부분 문자열')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 문자열

## 풀이

### 접근

- `LCS`

### 점화식

```python
if s[i - 1] == t[j - 1]:
    dp[i][j] = dp[i - 1][j - 1] + 1
    result = max(result, dp[i][j])
```

### 설계

- `LCS` 구현
