# BAEKJOON ONLINE JUDGE - 1389. 케빈 베이컨의 6단계 법칙

- [문제출처](https://www.acmicpc.net/problem/1389 "1389. 케빈 베이컨의 6단계 법칙")

## 알고리즘 분류

- 그래프 이론
- 그래프 탐색
- 너비 우선 탐색
- 플로이드-워셜

## 풀이

### 접근

- 플로이드-워셜

### 설계

- `INF(임의의 큰 수)`를 값으로 가지는 인접 행렬 생성
- 인접 행렬의 `y,x` 인덱스가 같은 부분은 `0`으로 처리
- `1 ~ n + 1` 까지 본인을 경유해서 갈 수 있으면서 최단 거리를 탐색하여 업데이트
- 탐색이 완료되면 본인 관계의 합을 구하고 가장 작은 인덱스 출력