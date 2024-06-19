# BAEKJOON ONLINE JUDGE - 3111. 검열

- [문제출처](https://www.acmicpc.net/problem/3111 '3111. 검열')
- [참고](https://rapun7el.tistory.com/284 '참고 블로그')

## 알고리즘 분류

- 구현
- 자료 구조
- 문자열
- 스택
- 덱

## 풀이

### 접근

- 스택 + 덱

### 설계

- `A` 문자열을 뒤집은 배열을 추가로 생성
- `T` 문자열을 덱으로 변환
- `front, back` 스택을 만들어 2번과 4번 알고리즘 수행
  - `T`에 `A`가 없을 때까지 반복 수행
- 알고리즘이 종료되면 `front, back` 두 배열에 걸쳐있는 `A`가 존재할 수 있으므로 `front`에 `back`을 집어넣으며 함수 수행
- 함수가 종료되면 `front` 출력
