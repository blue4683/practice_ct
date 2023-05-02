# BAEKJOON ONLINE JUDGE - 1708. 볼록 껍질

* [문제출처](https://www.acmicpc.net/problem/1708 "1708. 볼록 껍질")

## 알고리즘 분류

- 기하학
- 볼록 껍질

## 풀이

### 접근

- `Convex Hull` 알고리즘

### 설계

- 좌표를 `y`좌표가 작은 순으로 `y`좌표가 같다면 `x`좌표가 작은순으로 정렬한다.
- 정렬한 뒤 `Monotone Chain` 기법으로 볼록 껍질 탐색
- 결과 출력

## 참고

- `Convex Hull`을 찾는 방법은 3가지가 있다.
    - `Jarvis March`
    - `Graham Scan`
    - `Monotone Chain`
- 여기서 `Graham Scan`과 `Monotone Chain`이 자주 보이는 듯하다.
    - `Graham Scan`은 좌표를 각도순으로 정렬한 뒤 탐색
    - `Monotone Chain`은 좌표를 `x축` 정렬 후 윗 껍질 탐색 후, `reverse`시켜 아랫 껍질을 탐색