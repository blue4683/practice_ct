# Programmers - Level 3. 단어 변환

* [문제출처](https://school.programmers.co.kr/learn/courses/30/lessons/43163 "Level 3. 단어 변환")

## 알고리즘 분류
- DFS/BFS

## 풀이

### 접근
- DFS로 접근

### 설계
- `answer`를 큰 수로 정의
- 방문 배열 정의
- DFS 수행
    - `depth`가 `answer`이상이면 더이상 탐색할 필요가 없으므로 종료
    - `begin`이 `target`과 같다면 `depth`와 `answer`비교 후 `answer`를 최솟값으로 최신화
    - 반복문으로 방문하지 않은 단어 탐색
        - `begin`과 `words`의 `i`번째 단어 `word`가 하나만 다른 경우 `begin`을 `word`로 대체하고 재귀
- 결과 출력