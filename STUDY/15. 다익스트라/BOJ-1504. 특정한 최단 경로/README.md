# BAEKJOON ONLINE JUDGE - 1504. 특정한 최단 경로

* [문제출처](https://www.acmicpc.net/problem/1504 "1504. 특정한 최단 경로")

## 알고리즘 분류

- 그래프 이론
- 다익스트라

## 풀이

### 설계

- 다익스트라를 통해 1번, v1번, v2번에서 출발했을 때의 최소 비용을 구한다.
- v1, v2를 무조건 지나야하기 때문에 `1 - v1 - v2 - n, 1 - v2 - v1 - n` 두 가지 경우를 고려해야한다.
    - 두 가지 경우 모두 `INF` 이상이라면 무조건 지나는 경우가 없기 때문에 `-1`을 출력한다.
    - 아니라면 두 가지 경우 중 최솟값을 출력한다.