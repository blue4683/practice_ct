# BAEKJOON ONLINE JUDGE - 20057. 마법사 상어와 토네이도

* [문제출처](https://www.acmicpc.net/problem/20057 "20057. 마법사 상어와 토네이도")

## 알고리즘 분류

- 구현
- 시뮬레이션

## 풀이

### 설계

- 델타 배열(8방향) 정의(서->남서->남->....->북서)
- `tornado` 함수를 통해 이동
    - 진행 방향은 반시계 방향으로 90도 회전했을 때 방문하지 않았다면 경로 변경
    - 아니라면 진행 방향 유지
- `scatter` 함수를 통해 모래의 흩어짐 구현
    - 진행 방향의 반시계 방향 순으로 퍼센트 정의 및 수행
    - 진행 방향에 흩어지는 곳의 거리가 두 칸인 곳이 있을 경우 거리가 두 칸인 곳 먼저 계산
        - `sand` 배열의 범위를 벗어나면 결과값에 더해줌
        - 범위 안인 경우 해당 위치에 더해줌
- 토네이도가 `(0, 0)`에 도달하는 경우 반복문 종료 및 결과 출력