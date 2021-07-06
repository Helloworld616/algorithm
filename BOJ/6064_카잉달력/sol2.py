# 시간초과

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


# 최대공약수 구하는 함수
# 유클리드 호제법을 위해 필요
def LCD(M, N):
    while(N):
        M, N = N, M % N
    return M


# 최소공배수 구하는 함수
# 유클리드 호제법 이용
def LSM(M, N):
    return (M * N) // LCD(M, N)


# main
T = int(input())

for _ in range(T):
    # 입력 받기
    M, N, x, y = map(int, input().split())
    # start
    # start는 정답이 되는 수. x로 초기화
    start = x
    while True:
        # start % N가 y와 같으면 정답 출력
        if start % N == y:
            print(start)
            break
        # start가 최소공배수보다 커도 루프가 안 끝나면 -1 출력
        if LSM(M, N) < start:
            print(-1)
            break
        # 답이 나오지 않았다면 start M만큼 증가
        start += M
