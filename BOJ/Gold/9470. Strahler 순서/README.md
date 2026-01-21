# BAEKJOON ONLINE JUDGE - 9470. Strahler 순서

- [문제출처](https://www.acmicpc.net/problem/9470 '9470. Strahler 순서')

## 알고리즘 분류

- 그래프 이론
- 방향 비순환 그래프
- 위상 정렬

## 풀이

### 접근

- `위상 정렬`

### 설계

- 위상 정렬로 순서대로 노드 탐색
  - 탐색하면서 노드의 Strahler 순서를 비교해 다음 노드의 순서를 업데이트
