# BAEKJOON ONLINE JUDGE - 27925. 인덕션

- [문제출처](https://www.acmicpc.net/problem/27925 '27925. 인덕션')

## 알고리즘 분류

- 다이나믹 프로그래밍

## 풀이

### 설계

- 온도를 나타내는 리스트를 3개 만들어 DP 수행
  - 인덕션의 온도를 변경하는 모든 경우의 수를 확인
  - `dp[i + 1][food[i]][y][z] = min(
    dp[i + 1][food[i]][y][z],
    dp[i][x][y][z] + change_temp(x, food[i]),
)`
