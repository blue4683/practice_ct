# BAEKJOON ONLINE JUDGE - 13265. 색칠하기

- [문제출처](https://www.acmicpc.net/problem/13265 '13265. 색칠하기')

## 알고리즘 분류

- 그래프 이론
- 그래프 탐색
- 너비 우선 탐색
- 깊이 우선 탐색
- 이분 그래프

## 풀이

### 접근

- `BFS`

### 설계

- 노드마다 탐색이 안된 경우 BFS 수행
  - 인접한 노드가 같은 색이면 impossible 출력
