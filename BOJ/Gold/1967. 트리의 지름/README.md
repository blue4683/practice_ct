# BAEKJOON ONLINE JUDGE - 1967. 트리의 지름

- [문제출처](https://www.acmicpc.net/problem/1967 '1967. 트리의 지름')

## 알고리즘 분류

- 그래프 이론
- 그래프 탐색
- 트리
- 깊이 우선 탐색

## 풀이

### 접근

- BFS 접근

### 설계

- 임의의 노드에서 가장 거리가 먼 노드는 지름에 해당하는 노드 중 하나임을 전제로 설계
- 모든 노드를 탐색하는 것이 아니라 1번 노드 탐색 후 최대 거리를 가지는 노드 탐색으로 최대 거리 탐색
