# BAEKJOON ONLINE JUDGE - 9879. Cross Country Skiing

- [문제출처](https://www.acmicpc.net/problem/9879 '9879. Cross Country Skiing')

## 알고리즘 분류

- 자료 구조
- 그래프 이론
- 그래프 탐색
- 이분 탐색
- 분리 집합
- 최소 스패닝 트리

## 풀이

### 접근

- `BFS` + 이분 탐색

### 설계

- `0`과 가장 높은 높이를 기준으로 이분 탐색 진행
  - 중간 높이를 기준으로 모든 웨이포인트를 지날 수 있으면 결과값 갱신 후 가장 높은 높이를 갱신하고, 그렇지 못하다면 낮은 높이를 갱신
