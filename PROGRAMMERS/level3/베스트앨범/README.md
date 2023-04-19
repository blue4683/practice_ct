# Programmers - Level 3. 베스트앨범

* [문제출처](https://school.programmers.co.kr/learn/courses/30/lessons/42579 "Level 3. 베스트앨범")

## 알고리즘 분류
- 해시

## 풀이

### 접근
- `Hash` + `PriorityQue`

### 설계
- `Dictionary` 활용
- `key=genre`, `value=(-plays,i)`, 여기서 플레이수가 많은 순서대로 정렬해야하기 때문에 `-`를 추가
- 동시에 장르별 플레이 수 저장
- 플레이 수가 많은 장르 순으로 정렬하고, 장르에서 플레이수가 많은 순서대로 출력(비어 있다면 다음 장르로)