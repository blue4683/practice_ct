# BAEKJOON ONLINE JUDGE - 11780. 플로이드 2

- [문제출처](https://www.acmicpc.net/problem/11780 '11780. 플로이드 2')

## 알고리즘 분류

- 그래프 이론
- 최단 경로
- 플로이드-워셜

## 풀이

### 접근

- `플로이드-워셜`

### 설계

- 각 도시별 최단 거리를 플로이드-워셜로 탐색
  - 두 도시의 최단 거리가 업데이트 될때 중간도시와 도착도시의 경로를 저장해두어 이후 경로 추적에 사용
