# Programmers - Level 2. 게임 맵 최단거리

* [문제출처](https://school.programmers.co.kr/learn/courses/30/lessons/1844 "Level 2. 게임 맵 최단거리")

## 알고리즘 분류
- DFS/BFS

## 풀이

### 접근
- BFS로 접근

> 주어진 조건을 확인하자(`maps`의 크기)

### 설계
- 전형적인 BFS 문제
- 방문배열에 지나온 칸 수를 저장
- 현재까지 방문한 칸이 앞으로 방문할 방문배열의 값보다 작으면 방문 아니라면 최소값이 아니므로 방문 X