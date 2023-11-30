# BAEKJOON ONLINE JUDGE - 7579. 앱

- [문제출처](https://www.acmicpc.net/problem/7579 '7579. 앱')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 배낭 문제

## 풀이

### 설계

- 비활성화 후 다시 활성했을 때 필요한 메모리를 기준으로 DP를 진행한다.
- `dp[i][j] = max(app + dp[i - 1][j - memory], dp[i - 1][j])`
