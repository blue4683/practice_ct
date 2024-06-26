# BAEKJOON ONLINE JUDGE - 2630. 색종이 만들기
* [문제출처](https://www.acmicpc.net/problem/2630 "2630. 색종이 만들기")

## 알고리즘 분류
- 분할 정복
- 재귀

## 풀이
### 접근
- 범위 안이 모두 같은 값인지 확인하고 아니라면 4등분하여 다시 진행한다.
- 재귀함수 사용

### 설계
1. 함수에 색종이의 왼쪽 밑 모서리의 좌표와 오른쪽 위 모서리의 좌표를 입력한다.
2. 함수에서 색종이 한 변의 길이와 확인할 색깔을 구한다.
3. 길이가 2보다 작다면 더이상 종이를 나눌 수 없으므로 흰색 또는 파란색 카운트를 1 증가시킨다.
4. 입력받은 좌표 범위를 탐색한다.
5. 범위 안에 색깔이 모두 같다면 흰색 또는 파란색 카운트를 1 증가시킨다.
6. 범위 안에 색깔이 다른 곳이 있다면 색종이를 4등분하고 좌표들을 함수에 넣고 위의 과정을 반복한다.(길이를 2로 나누어 좌표에 더해줘서 좌표를 설정한다.)