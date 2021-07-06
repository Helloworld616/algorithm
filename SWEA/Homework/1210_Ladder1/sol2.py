import sys
sys.stdin = open("input.txt")

def solution(M):
    N = len(M)
    next = 'U'
    y = N - 1
    for x in range(N):
        last_row = M[y]
        if last_row[x] == 2:
            while y > 0:
                # 올라갈 때, 좌/우회전 우선
                if next == 'U':
                    if x < N - 1 and M[y][x + 1]: # 우회전
                        next = 'R'
                        x += 1
                    elif x > 0 and M[y][x - 1]: # 좌회전
                        nxt = 'L'
                        x -= 1
                    else: # 직진
                        y -= 1
                else:
                    y -= 1
            else: # 횡보 중에는 올라가기 우선
                if M[y - 1][x]:
                    nxt = 'U'
                    y -= 1
                elif nxt == 'R':
                    x += 1
                elif nxt == 'L':
                    x -= 1

        return x

T = 10
N = 7
for _ in range(1, T+1):
    tc = int(input())
    matrix = []
    for _ in range(N):
        matrix.append()
