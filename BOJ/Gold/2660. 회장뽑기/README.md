# BAEKJOON ONLINE JUDGE - 2660. 회장뽑기

- [문제출처](https://www.acmicpc.net/problem/2660 '2660. 회장뽑기')

## 알고리즘 분류

- 그래프 이론
- 그래프 탐색
- 너비 우선 탐색
- 최단 경로
- 플로이드-워셜

## 풀이

### 접근

- 구현

### 설계

- 회원마다 이어져있는 회원들을 탐색
- 방문 배열에 거쳐간 회원수의 최솟값을 저장하고 모두 방문했다면 그 중에서 가장 큰 값을 결과 배열에 저장
- 결과 배열에서 가장 작은 값을 출력하고 그에 해당하는 인덱스를 출력
