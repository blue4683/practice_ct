# BAEKJOON ONLINE JUDGE - 10775. 공항

- [문제출처](https://www.acmicpc.net/problem/10775 '10775. 공항')

## 알고리즘 분류

- 자료 구조
- 그리디 알고리즘
- 분리 집합

## 풀이

### 접근

- 유니온 파인드

### 설계

- 이중 반복문으로는 시간 초과 발생 -> 유니온 파인드를 통해 비행기의 도킹 여부 확인
- `g`번 비행기를 도킹 시키기 위해 `find`를 통해 가능 여부 확인
  - `find(g)`에서 `0`이라면 이미 이전 번호들은 차있으므로 도킹 불가
  - `find(g)`가 `0`이 아니라면 비어있는 번호가 있으므로 도킹 가능
  - `g`번 비행기를 도킹 시켰다면 `g - 1`번과 유니온 파인드 수행
    - 만약 `g - 1` 전에 비어있는 번호가 있다면 그 번호가 저장될 것이고, 아니라면 `0`이 저장됨
