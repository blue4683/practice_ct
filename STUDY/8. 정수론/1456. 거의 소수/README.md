# BAEKJOON ONLINE JUDGE - 1456. 거의 소수

* [문제출처](https://www.acmicpc.net/problem/1456 "1456. 거의 소수")

## 알고리즘 분류
- 수학
- 정수론
- 소수 판정
- 에라토스테네스의 체

## 풀이

### 설계
- 에라토스테네스의 체로 구현
- 소수를 구하는 것이 아닌 소수의 제곱수들을 찾기 때문에 범위의 제곱근까지만 탐색 가능
- 소수의 제곱부터 소수를 곱해줘서 범위 안에 있으면 카운트 증가