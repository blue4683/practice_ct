# BAEKJOON ONLINE JUDGE - 18352. 특정 거리의 도시 찾기

* [문제출처](https://www.acmicpc.net/problem/18352 "18352. 특정 거리의 도시 찾기")

## 알고리즘 분류
- 그래프 이론
- 그래프 탐색
- 너비 우선 탐색
- 다익스트라

## 풀이
### 설계
- 인접리스트로 그래프 구현
- `BFS` + 방문 배열에 자신이 지나온 노드의 수 저장
- 탐색 중 자신이 지나온 노드의 수가 방문 배열에 저장되어 있는 수보다 작으면 탐색 아니라면 탐색 X
- 방문 배열이 `K`인 인덱스 출력