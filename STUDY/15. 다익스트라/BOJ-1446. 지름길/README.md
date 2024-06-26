# BAEKJOON ONLINE JUDGE - 1446. 지름길

* [문제출처](https://www.acmicpc.net/problem/1446 "1446. 지름길")

## 알고리즘 분류

- 다이나믹 프로그래밍
- 그래프 이론
- 다익스트라

## 풀이

### 설계

- 입력받은 고속도로 길이만큼 배열을 생성한다.
    - 배열에 저장되는 값은 저장되는 위치의 인덱스와 같도록 한다.
- 입력받은 지름길의 시작위치를 기준으로 `heapq`에 저장한다.
- `0`과 가까운 지름길부터 가져와 지름길을 사용할 때의 거리와 사용하지 않을 때의 거리를 비교하여 최솟값을 갱신한다.
    - 만약 지름길을 사용한 경우가 거리가 더 짧다면, 그 뒤의 거리는 지름길을 사용한 거리로 변경해준다.
- 모든 지름길을 확인한 뒤 도착지점의 거리를 출력한다.