# BAEKJOON ONLINE JUDGE - 5827. What's Up With Gravity

- [문제출처](https://www.acmicpc.net/problem/5827 '5827. What's Up With Gravity')

## 알고리즘 분류

- 구현
- 그래프 이론
- 시뮬레이션
- 최단 경로
- 다익스트라
- 0-1 너비 우선 탐색

## 풀이

### 접근

- 다익스트라 + `BFS`

### 설계

- 중력을 뒤집는 횟수를 기준으로 다익스트라 BFS 탐색 진행
- 현재 위치에서 이동하기 전에 방문 배열에 상하좌우로 이동한 이력을 비트마스킹으로 저장
