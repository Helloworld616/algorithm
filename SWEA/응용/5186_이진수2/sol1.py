import sys
sys.stdin = open('sample_input.txt')


# 이진수 변환 함수
def to_binary(N):
    # 이진수 결과 초기화
    binary = ''

    # N이 0 이하가 될 때까지 반복문 실행
    while N > 0:
        # N을 2배 더한 값을 변수 double에 할당
        double = N*2
        # double의 정수 부분만 추출해서 binary에 합산
        binary += str(int(double))
        # binary의 길이가 12를 넘어가면 overflow 반환
        if len(binary) > 12:
            return 'overflow'
        # doble의 소수 부분만을 N에 할당
        N = double - int(double)

    # 이진수 변환 결과 반환
    return binary


# main
T = int(input())

for tc in range(1, T+1):
    # N 입력 받기
    # 주의! 실수로 입력 받아야 함!
    N = float(input())
    # 이진수 변환 결과 출력
    print('#{} {}'.format(tc, to_binary(N)))
