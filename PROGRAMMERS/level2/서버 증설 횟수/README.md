# Programmers - Level 2. 서버 증설 횟수

- [문제출처](https://school.programmers.co.kr/learn/courses/30/lessons/389479 'Level 2. 서버 증설 횟수')

## 풀이

### 접근

- `큐`

### 설계

- 서버를 증설한 시간을 큐에 저장하고 시간이 만료되면 큐에서 꺼냄
- 현재 필요한 서버의 수보다 서버의 개수가 작으면 부족한 만큼 큐에 현재 시간을 저장하고 결과값에 더해줌
