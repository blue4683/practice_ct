# BAEKJOON ONLINE JUDGE - 11965. Bessie's Dream

- [문제출처](https://www.acmicpc.net/problem/11965 "11965. Bessie's Dream")

## 알고리즘 분류

- 그래프 이론
- 그래프 탐색
- 너비 우선 탐색
- 최단 경로
- 다익스트라

## 풀이

### 접근

- 다익스트라

### 설계

- 힙을 사용해 이동을 최소로 하는 경우를 탐색
  - `y, x, smell` 상태에 따라 `visited` 배열에 저장하며 불필요한 탐색 방지(시간초과 방지)
- 조건에 따라 구현
