# Programmers - Level 3. 여행경로

* [문제출처](https://school.programmers.co.kr/learn/courses/30/lessons/43164 "Level 3. 여행경로")

## 알고리즘 분류
- DFS/BFS

## 풀이

### 접근
- DFS로 접근

### 설계
- 도착 지점 사전 순으로 내림차순 정렬
- DFS 수행
- `result`에 여행경로 저장하면서 진행
- 모든 티켓을 탐색했다면 `answer`에 `result` 저장
- 결국 가장 마지막에 찾은 경우를 `answer`에 저장하게 되고 여기서는 도착 지점의 사전 순으로 빠른 경우가 저장된다.