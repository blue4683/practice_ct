# BAEKJOON ONLINE JUDGE - 3482. Labyrinth

- [문제출처](https://www.acmicpc.net/problem/3482 '3482. Labyrinth')

## 알고리즘 분류

- 그래프 이론
- 그래프 탐색
- 트리
- 깊이 우선 탐색

## 풀이

### 접근

- `BFS`

### 설계

- 하나의 점을 잡아 BFS로 이동하는 거리 탐색
- BFS로 탐색한 가장 먼 거리에 있는 점을 기준으로 재탐색 후 로프의 최대 길이 갱신
