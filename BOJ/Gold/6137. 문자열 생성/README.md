# BAEKJOON ONLINE JUDGE - 6137. 문자열 생성

- [문제출처](https://www.acmicpc.net/problem/6137 '6137. 문자열 생성')

## 알고리즘 분류

- 그리디 알고리즘
- 문자열
- 투 포인터

## 풀이

### 접근

- 그리디 + 투 포인터

### 설계

- 주어진 문자열의 처음과 끝을 비교해서 먼저 더할 문자를 탐색
  - 만약 처음과 끝이 같다면 문자가 달라질때까지 처음 인덱스를 증가시키고, 끝 인덱스를 감소시켜서 탐색
- 문자열의 길이가 `80`이 되면 출력 후 문자열을 초기화
