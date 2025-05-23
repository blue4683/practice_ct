# BAEKJOON ONLINE JUDGE - 1477. 휴게소 세우기

- [문제출처](https://www.acmicpc.net/problem/1477 '1477. 휴게소 세우기')

## 알고리즘 분류

- 이분 탐색
- 매개 변수 탐색

## 풀이

### 접근

- 이분 탐색

### 설계

- 현재 휴게소와 이전 휴게소의 거리가 `mid` 이상일 때 `mid`로 나눈 몫만큼 휴게소를 설치
- 끝까지 탐색하고 설치한 휴게소가 `m`개 이하일 경우 결과값을 `mid`로 갱신하고 끝 인덱스를 `mid - 1`로 갱신
- 아니라면 시작 인덱스를 `mid + 1`로 설정
- 시작이 끝보다 커지면 이분 탐색 종료
