# Programmers - Level 3. 퍼즐 조각 채우기

* [문제출처](https://school.programmers.co.kr/learn/courses/30/lessons/84021 "Level 3. 퍼즐 조각 채우기")

## 알고리즘 분류
- DFS/BFS

## 풀이

### 설계
- `game_board`와 `table`에서 각각 빈칸과 퍼즐조각을 찾는다.
    - 찾을 때 BFS로 배열을 탐색하고, `flag`를 통해 각각 `0`과 `1`을 찾는다.
    - 탐색으로 해당 위치의 좌표를 저장하고 `normalize`함수를 통해 좌표를 정규화한 후 이차원 배열로 변환한다.
- 정규화한 빈칸과 퍼즐조각을 서로 비교하여 맞으면 그 빈칸만큼의 `1`의 수를 `answer`에 더한다.
    - 비교할 때 `rotated_arr` 함수를 통해 90도씩 돌리면서 비교한다.