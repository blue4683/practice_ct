# Programmers - Level 3. 네트워크

* [문제출처](https://school.programmers.co.kr/learn/courses/30/lessons/43162 "Level 3. 네트워크")

## 알고리즘 분류
- DFS/BFS

## 풀이

### 접근
- 유니온 파인드로 접근

### 설계
- `answer`를 `n`으로 정의
- 그래프 생성 후 자신의 번호를 해당하는 인덱스에 저장
- `computers` 인접 행렬을 탐색하면서 서로 연결되어 있다면 부모 노드가 같은지 확인
- 같으면 넘어가고 다르다면 `union` 수행 후 `answer` 1 감소
- 인접 행렬을 모두 탐색하면 결과 리턴