# BAEKJOON ONLINE JUDGE - 8980. 택배

- [문제출처](https://www.acmicpc.net/problem/8980 '8980. 택배')

## 알고리즘 분류

- 그리디 알고리즘
- 정렬

## 풀이

### 접근

- 정렬

### 설계

- 도착지를 오름차순으로 정렬
- 마을 번호를 인덱스로 가지는 트럭 용량을 나타내는 배열 생성
- 출발 ~ 도착까지 트럭 용량에서 박스 개수를 빼거나 트럭 용량이 더 작을경우 트럭 용량을 뺌
- 뺀 박스를 결과값에 더함
