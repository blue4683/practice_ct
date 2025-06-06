# BAEKJOON ONLINE JUDGE - 1162. 도로포장

- [문제출처](https://www.acmicpc.net/problem/1162 '1162. 도로포장')

## 알고리즘 분류

- 다이나믹 프로그래밍
- 그래프 이론
- 최단 경로
- 다익스트라

## 풀이

### 접근

- `다익스트라` + `DP`

### 설계

- 포장하는 횟수에 따른 최솟값을 저장해 사용하기 위해 DP 테이블 생성
  - 다익스트라로 탐색하면서 비용을 지불하는 방법과 포장하는 횟수가 있을 때 비용을 지불하지 않고 넘어가는 방법을 동시에 탐색
