# BAEKJOON ONLINE JUDGE - 1987. 알파벳

* [문제출처](https://www.acmicpc.net/problem/1987 "1987. 알파벳")

## 알고리즘 분류
- 그래프 이론
- 그래프 탐색
- 깊이 우선 탐색
- 백트래킹

## 풀이
### 1차 시도
- DFS로 접근
- `path`를 통해 지나온길을 확인하고 알파벳이 `path`에 없으면 `depth+1` 수행
- 재귀마다 `result`값 갱신
- 시간초과

### 2차 시도
- BFS로 접근
- `set`을 통해 한 좌표에 동일한 `path`를 가진 경우의 중복을 제거
- `q`에서 꺼낼때마다 `result`값 갱신