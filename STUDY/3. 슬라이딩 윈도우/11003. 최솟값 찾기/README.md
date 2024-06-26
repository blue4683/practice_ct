# BAEKJOON ONLINE JUDGE - 11003. 최솟값 찾기

* [문제출처](https://www.acmicpc.net/problem/11003 "11003. 최솟값 찾기")

## 알고리즘 분류
- 자료 구조
- 우선순위 큐
- 덱

## 풀이
### 접근
- 범위가 `1 ≤ L ≤ N ≤ 5,000,000`으로 이중 반복문을 사용하면 시간초과 예상
- 범위를 이동하면서 문제 해결(슬라이딩 윈도우)

### 설계
- i-L+1이 0이하이면 0~i사이의 최솟값 출력
- Ai가 작은 순으로 리스트에 저장
- 최솟값의 인덱스를 기억하고 있다가 범위 밖으로 나가면 다른 최솟값을 가져와야함
- i-L+1이 0보다 커지면서 최솟값이 사라지거나 갱신되면 리스트 맨 처음 값을 제거하고 그 다음에 있는 최솟값을 쓰거나 새로운 최솟값을 맨 앞에 넣고 사용
- 기존의 최솟값의 위치보다 뒤에 있으면서 더 작다면 이전의 최솟값을 제거하고 새로운 최솟값을 저장

### 1차시도(시간초과)
- 테스트케이스 끝 부분에서 시간초과로 인한 오답

### 2차시도
- 1차시도 코드에서 최솟값 리스트를 덱(`Deque`)으로 구현
- 정답

## 관련 개념
### `Deque`과 `List`의 차이
- 리스트(`List`)는 첫번째 원소를 `pop`을 하기 위해서는 원소를 꺼낸 뒤 뒤에 있는 모든 원소들을 앞으로 이동시키기 때문에 `O(n)`의 시간복잡도를 가짐
- 덱(`Deque`)은 `double-linked list`로 구현된 `Double-ended Queue`로 양 끝의 원소를 추가/삭제할 수 있는 자료구조, `popleft`를 사용하여 첫번째 원소를 꺼내는데 `O(1)`의 시간복잡도를 가짐