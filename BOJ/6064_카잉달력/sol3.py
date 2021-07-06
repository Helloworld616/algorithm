import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


# main
T = int(input())

for _ in range(T):
    # 입력 받기
    M, N, x, y = map(int, input().split())
    # start
    # start는 정답이 되는 수. x로 초기화
    start = x
    while True:
        # start-y를 N으로 나눈 나머지가 y와 같으면 정답 출력
        # start가 아닌 start - y를 검사하는 이유는 start % y == 0인 경우도 고려하기 위함임
        if (start - y) % N == 0:
            print(start)
            break
        # start가 M * N보다 커도 루프가 안 끝나면 -1 출력
        if M * N < start:
            print(-1)
            break
        # 답이 나오지 않았다면 start M만큼 증가
        start += M