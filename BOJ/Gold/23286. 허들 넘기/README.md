# BAEKJOON ONLINE JUDGE - 23286. 허들 넘기

- [문제출처](https://www.acmicpc.net/problem/23286 '23286. 허들 넘기')

## 알고리즘 분류

- 그래프 이론
- 최단 경로
- 다익스트라
- 플로이드-워셜

## 풀이

### 접근

- `플로이드`

### 설계

- 그래프에 두 지점을 가는 경로 중 가장 높은 허들의 높이가 최소가 되는 값을 저장하고 플로이드 수행
- 값이 `INF`인 경우 가지 못하는 곳이므로 `-1`으로 변환하여 출력
