# BAEKJOON ONLINE JUDGE - 12930. 두 가중치

- [문제출처](https://www.acmicpc.net/problem/12930 '12930. 두 가중치')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 그래프 이론
- 최단 경로
- 다익스트라

## 풀이

### 접근

- `다익스트라`

### 설계

- `heap`을 사용해 다익스트라 탐색 진행
  - 우선순위 기준을 (이동 비용, 가중치1, 가중치2, 노드 번호) 순으로 지정해 탐색 수행
  - 두 가중치 중 작은 것이 있다면 비용이 줄어들 수 있기 때문
