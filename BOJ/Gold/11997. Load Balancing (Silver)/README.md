# BAEKJOON ONLINE JUDGE - 11997. Load Balancing (Silver)

- [문제출처](https://www.acmicpc.net/problem/11997 '11997. Load Balancing (Silver)')

## 알고리즘 분류

- 브루트포스
- 누적 합
- 값 / 좌표 압축

## 풀이

### 접근

- 좌표 압축 + 누적 합

### 설계

- 주어진 좌표의 범위가 주어진 좌표의 개수보다 매우 크기 때문에 좌표 압축을 통해 범위를 제한
- 압축한 좌표를 n x n 배열에 매핑
- 이후 특정 (x, y)를 기준으로 어느 사분면에 있는지를 누적합으로 구한 뒤 최솟값 갱신
