import sys
sys.stdin = open('input.txt')


# 판별 함수
# 정수를 2로 나누면 이진수의 마지막 비트부터 차례대로 구할 수 있다.
# 나머지가 비트가 된다.
def decide(N, M):
    # N이 0이 될 때까지 반복문 실행
    while N:
        # 만약 2로 나눈 나머지가 0이 나올 경우 바로 OFF 반환
        if not M % 2:
            return 'OFF'
        # 시프트 연산자를 통해 M을 2로 나누고 (이렇게 하면 실행시간이 훨씬 빨라짐!)
        M >>= 1
        # N에서 1을 뺸다.
        N -= 1
    # 반복문 실행 내내 한 번도 0이 안 나왔을 경우 ON 반환
    return 'ON'


# main
T = int(input())

for tc in range(1, T+1):
    # N과 M 입력 받기
    N, M = map(int, input().split())
    # 판변 결과 출력
    print('#{} {}'.format(tc, decide(N, M)))

