# BAEKJOON ONLINE JUDGE - 5901. Relocation

- [문제출처](https://www.acmicpc.net/problem/5901 '5901. Relocation')

## 알고리즘 분류

- 그래프 이론
- 브루트포스
- 최단 경로
- 다익스트라

## 풀이

### 접근

- 다익스트라 + 조합

### 설계

- 마트에서 다른 마을까지의 최소 거리를 구해 저장
- 마트를 순회하는 경우의 수를 `permutations`로 생성한 뒤 모든 경우의 수에 대해 거리를 계산하여 최솟값 갱신
