import sys
sys.stdin = open('sample_input.txt')

# 16진수를 2진수로 변환해주는 딕셔너리
to_binary = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
             '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
             'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

# main
T = int(input())

for tc in range(1, T+1):
    # N과 16진수 입력 받기
    N, hexa = input().split()

    # 이진수 변환 결과 초기화
    binary = ''
    # 딕셔너리 to_binary를 이용하여
    # 16진수 안의 숫자들을 2진수로 변경해서
    # binary에 추가
    for number in hexa:
        binary += to_binary[number]

    # binary 출력
    print('#{} {}'.format(tc, binary))
