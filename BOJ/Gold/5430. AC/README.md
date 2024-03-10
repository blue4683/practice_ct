# BAEKJOON ONLINE JUDGE - 5430. AC

- [문제출처](https://www.acmicpc.net/problem/5430 '5430. AC')

## 알고리즘 분류

- 구현
- 자료 구조
- 문자열
- 파싱
- 덱

## 풀이

### 설계

- `deque`을 활용해 구현
  - 뒤집는 횟수를 기억하고, 홀수 일때는 뒤에서 짝수 일대는 앞에서 하나씩 `pop`을 수행
  - 모든 함수를 수행한 뒤 뒤집는 횟수가 홀수이면 `reverse`후에 출력
