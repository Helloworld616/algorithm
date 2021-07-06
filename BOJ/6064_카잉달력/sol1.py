# 시간초과

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    first, second = 1, 1
    cnt = 1
    while True:
        # 첫번째 수와 두번째 수가 x, y와 같으면 순서 출력
        if first == x and second == y:
            print(cnt)
            break
        # 첫번째 수와 두번째 수가 다시 <1:1>로 돌아왔는데도 루프를 못 빠져나갔다면 -1 출력
        elif first == 1 and second == 1 and cnt > 1:
            print(-1)
            break
        # first, second, cnt 1 증가
        first += 1
        second += 1
        cnt += 1
        # 정해진 범위를 넘겼을 경우 다시 1로 초기화
        if first > M:
            first = 1
        if second > N:
            second = 1
