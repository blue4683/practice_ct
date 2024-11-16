# BAEKJOON ONLINE JUDGE - 18606. Block Breaker

- [문제출처](https://www.acmicpc.net/problem/18606 '18606. Block Breaker')

## 알고리즘 분류

- 구현
- 시뮬레이션
- 재귀

## 풀이

### 접근

- `BFS`

### 설계

- 블럭을 제거하는 위치를 기준으로 BFS 탐색
  - 좌우, 상하 각각 블럭이 하나 이상 없는 경우 큐에 추가하며 탐색
