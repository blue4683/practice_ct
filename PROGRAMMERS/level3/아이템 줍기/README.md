# Programmers - Level 3. 아이템 줍기

* [문제출처](https://school.programmers.co.kr/learn/courses/30/lessons/87694 "Level 3. 아이템 줍기")

## 알고리즘 분류
- DFS/BFS

## 풀이

### 접근
- BFS로 접근

### 설계
> - 변과 변 사이의 거리가 1인 경우 경로를 벗어나는 현상을 방지하기 위해 좌표를 두배로 늘림
- 사각형의 테두리를 제외한 모든 영역을 -1로 설정
- BFS로 탐색
- 지나온 칸의 수만큼 `graph`배열에 저장하면서 진행
- 목적지에 도착하면 해당 인덱스에 저장된 값을 `2`로 나눈 뒤 출력