# BAEKJOON ONLINE JUDGE - 1744. 수 묶기

* [문제출처](https://www.acmicpc.net/problem/1744 "1744. 수 묶기")

## 알고리즘 분류
- 그리디 알고리즘
- 정렬
- 많은 조건 분기

## 풀이
### 접근
- 가장 큰 수열의 합을 구하기 위한 조건은 다음과 같다.
1. `1`은 묶지 않고 더한다. (곱했을 때 값이 변하지 않아 오히려 합이 작아진다.)
2. `1`과 `0`을 제외한 양수는 큰 수끼리 서로 곱한다.
3. 음수는 절대값이 큰 음수끼리 서로 곱한다.
4. 음수의 개수가 홀수일 때 남은 음수를 처리할 때 `0`이 있는 경우 `0`과 곱해 `0`으로 만들고, 없다면 그대로 결과에 더해준다.

### 설계
- 양수, 음수, `0`과 `1`은 각각 `plus`, `minus`, `amb` 리스트에 저장한다.
- 그 후 양수 리스트는 내림차순으로 음수 리스트는 오름차순으로 정렬한다.
- 양수 리스트의 인덱스를 `2`씩 증가시키며 `i`와 `i + 1`번째 값들을 곱한 뒤 `result` 리스트에 저장한다. 양수 개수가 홀수라면 마지막 남은 수도 `result`에 그대로 저장한다.
- 마찬가지로 음수 리스트의 인덱스를 `2`씩 증가시키며 `i`와 `i + 1`번째 값들을 곱한 뒤 `result` 리스트에 저장한다. 음수 개수가 홀수라면 남은 수를 `rest`리스트에 저장한다.
- `rest` 리스트에 값이 존재하고, `amb` 리스트에 `0`이 존재한다면 둘이 곱해서 `0`으로 만들 수 있기 때문에 따로 처리하지 않는다. 반대로 `0`이 존재하지 않는다면 `result`에 `rest`에 있는 음수를 저장한다.
- `amb`에 값이 들어있다면 마찬가지로 `result`에 저장한다.
- `result`의 합을 반환하여 출력한다.