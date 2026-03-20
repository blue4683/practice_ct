# BAEKJOON ONLINE JUDGE - 20046. Road Reconstruction

- [문제출처](https://www.acmicpc.net/problem/20046 '20046. Road Reconstruction')

## 알고리즘 분류

- 그래프 이론
- 그래프 탐색
- 최단 경로
- 다익스트라
- 격자 그래프

## 풀이

### 접근

- `다익스트라`

### 설계

- BFS로 탐색하면 모든 경우의 수 탐색으로 시간 초과가 발생하므로 항상 최소 비용을 우선으로 탐색하기 위해 `heap`을 사용한 다익스트라 구현
