# BAEKJOON ONLINE JUDGE - 2251. 물통

* [문제출처](https://www.acmicpc.net/problem/2251 "2251. 물통")

## 알고리즘 분류
- 그래프 이론
- 그래프 탐색
- 너비 우선 탐색
- 깊이 우선 탐색

## 풀이
### 설계
- 책 참고
- 주어진 노드의 경우들을 가지고 그래프를 역으로 생성하는 문제
- 노드에서 갈 수 있는 경우로 그래프 생성, 이미 방문한 경우라면 큐에 추가 X
- 물통이 빌 때까지 다른 물통에 저장하고, 물통이 넘친다면 초과하는 값만큼 빈 물통에 넣는다.
- 큐에 추가할 때 1번째 물통이 비어있다면 3번째 물통의 값을 정답 리스트에 추가한다.