# SKOJ - 큐 시뮬레이터 만들기

- [문제출처](https://skoj.site/problem/10042 '큐 시뮬레이터 만들기')

## 풀이

### 접근

- `큐(Deque)`

### 설계

- 입력 명령을 공백 기준으로 파싱해 `push`, `pop`, `size`, `empty`, `front`, `back` 6가지 연산을 `deque` 메서드로 각각 O(1)에 처리
- `pop`, `front`, `back`은 큐가 비어 있는지 조건부 표현식으로 먼저 검사해 `-1`과 실제 값을 구분해 출력
