# BAEKJOON ONLINE JUDGE - 1987. 알파벳

- [문제출처](https://www.acmicpc.net/problem/1987 '1987. 알파벳')

## 알고리즘 분류

- 그래프 이론
- 그래프 탐색
- 깊이 우선 탐색
- 백트래킹

## 풀이

### 설계

- DFS로 접근
- `visited` 배열에 `ord(s) - ord('A')` 위치에 방문한 값을 갱신하면서 탐색
- 재귀마다 `result`값 갱신
