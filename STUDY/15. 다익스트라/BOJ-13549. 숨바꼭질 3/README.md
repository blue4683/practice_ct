# BAEKJOON ONLINE JUDGE - 13549. 숨바꼭질 3

* [문제출처](https://www.acmicpc.net/problem/13549 "13549. 숨바꼭질 3")

## 알고리즘 분류

- 그래프 이론
- 그래프 탐색
- 너비 우선 탐색
- 다익스트라
- 0-1 너비 우선 탐색

## 풀이

### 설계

- 가장 큰 수로 최대 길이만큼 일차원 배열을 생성한다.
    - 현재 위치의 값을 `0`으로 변경한다.
- `heapq`에 `[현재 위치에 도달하는 최소 비용, 현재 위치]`를 담으면서 `BFS` 탐색을 진행한다.
    - 현재 위치에서 이동한 비용이 탐색한 위치에 저장되어 있는 비용보다 작다면 갱신해준다.
- 모든 위치에서의 최소 비용을 구한 뒤 `k` 위치의 비용을 출력한다.