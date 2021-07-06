# 첫 번째 코드

import sys
sys.stdin = open('sample_input.txt')

# 16진수를 2진수로 변환하는 딕셔너리
to_binary = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
             '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
             'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

# 비율에 따라 2진수를 10진수로 변환하는 딕셔너리
# 이 딕셔너리의 key는 모두 "1의 비율 : 0의 비율 : 1의 비율"을 나타낸다
to_decimal = {'112': '0', '122': '1', '221': '2', '114': '3', '231': '4', '132': '5',
              '411': '6', '213': '7', '312': '8', '211': '9'}


# 16진수 코드를 2진수 코드로 변환하는 함수
def change_to_binary():
    # 2진수 코드들을 담을 리스트 생성
    # 리스트를 생성하는 이유는, 코드가 2개 이상일 수도 있기 때문!
    binary_codes = []

    # 16진수 코드에서 코드를 한 줄씩 꺼낸다
    for code in barcode:
        # 2진수 변환 결과 초기화
        binary_code = ''
        # 16진수 코드에 존재하는 0의 갯수를 셀 변수. 0으로 초기화.
        zero_cnt = 0

        # 코드 안의 글자들을 하나씩 꺼낸다
        for char in code:
            # to_binary 딕셔너리를 이용해 16진수 글자를 2진수로 해석
            # 해석 결과를 변환 결과에 더한다
            binary_code += to_binary[char]
            # 만약 글자가 0일 경우 zero_cnt 1 증가
            if char == '0':
                zero_cnt += 1

        # 2진수 변환 결과가 결과 리스트에 없고
        # zero_cnt가 코드의 길이와 다를 경우 (= 코드가 전부 0이 아닐 경우 = 코드 안에 암호가 있을 경우)
        if binary_code not in set(binary_codes) and zero_cnt != len(code):
            # 결과 리스트에 변환 결과 추가
            binary_codes.append(binary_code)

    # 결과 리스트 반환
    return binary_codes


# 2진수 코드를 10진수 코드로 변환하는 함수
def change_to_decimal():
    # 10진수 코드들을 담을 리스트 생성
    # 리스트를 생성하는 이유는, 코드가 2개 이상일 수도 있기 때문!
    decimal_codes = []
    # 비율 정보를 나타내는 리스트 ratio 생성
    ratio = [0, 0, 0]
    # 리스트 ratio의 인덱스를 -1로 초기화
    ratio_idx = -1
    # 암호 출현 여부를 캐치하기 위한 변수 signal
    signal = '0'
    # flag 변수를 생성하여 False로 초기화
    flag = False

    # 2진수 코드에서 코드를 한 줄씩 꺼낸다
    for code in binary:
        # 10진수 변환 결과 초기화
        decimal_code = ''

        # 코드의 끝에서부터 검사. 코드에서 글자를 하나씩 꺼낸다.
        # 끝에서부터 검사하는 이유는, 모든 암호가 끝에 1을 가지는 공통점을 가지고 있기 때문!
        # 이에 반해 앞에는 전부 0이라서 앞에서부터 검사하면 암호를 판별하기 힘들다.
        for i in range(len(code) - 1, -1, -1):
            # 글자가 signal과 다를 경우 (= 암호 패턴이 바뀔 경우)
            if code[i] != signal:
                # signal을 현재 글자로 변경
                signal = code[i]
                # ratio_idx에 1을 합산
                ratio_idx += 1
                # flag를 True로 변경
                flag = True

                # 만약 ratio_idx가 2보다 클 경우 (= 하나의 암호가 판별이 끝났을 경우)
                if ratio_idx > 2:
                    # 비율을 정제한 결과를 담을 리스트 temp 생성
                    temp = []

                    # 비율 정제화 과정
                    # ratio에서 비율을 하나씩 꺼낸다
                    for rate in ratio:
                        # 비율을 ratio의 최솟값으로 나눈 결과를 temp에 추가
                        temp.append(rate // min(ratio))

                    # 10진수 변환 결과에, 비율을 10진수로 바꾼 값을 더한다.
                    # 주의할 점! 현재 탐색을 끝에서부터 하고 있으므로 여기서의 덧셈도 끝에서부터 이루어져야 한다.
                    decimal_code = to_decimal[''.join(list(map(str, temp)))] + decimal_code

                    # 10진수 변환 결과의 길이가 8이 되었을 경우
                    # 결과 리스트에 변환 결과를 추가하고
                    # 10진수 변환 결과를 다시 초기화
                    if len(decimal_code) == 8:
                        decimal_codes.append(decimal_code)
                        decimal_code = ''

                    # 비율 리스트와 비율 리스트의 인덱스 초기화
                    ratio = [0, 0, 0]
                    ratio_idx = -1
                    # flag를 False로 변경
                    flag = False

            # flag가 True일 경우 비율 계산 진행
            if flag:
                ratio[ratio_idx] += 1

    # 결과 리스트 반환
    return decimal_codes


# 암호 코드를 검증하는 함수
def cal():
    # 반환할 정답을 0으로 초기화
    ans = 0

    # 10진수 코드를 하나씩 꺼낸다
    for decimal_code in decimal_complete:
        # 홀수 자리의 합산 값과 짝수 자리의 합산 값을 0으로 초기화
        odd = 0
        even = 0

        # 10진수 코드의 자릿수를 계산한다
        # 인덱스가 0부터 시작하므로 짝수 인덱스가 홀수 번째, 홀수 인덱스가 짝수 번째 수이다!
        for i in range(len(decimal_code)):
            # 인덱스가 홀수일 경우 even에 숫자 합산
            if i % 2:
                even += int(decimal_code[i])
            # 인덱스가 짝수일 경우 odd에 숫자 합산
            else:
                odd += int(decimal_code[i])

        # odd를 3배한 값과 even을 합산한 결과를 저장
        total = odd * 3 + even
        # 합산 결과가 10으로 나누어 떨어지면 ans에 10진수 코드의 총합을 더한다
        if not total % 10:
            ans += sum(list(map(int, list(decimal_code))))

    # 최종 결과 ans 반환
    return ans


# main
T = int(input())

for tc in range(1, T + 1):
    # N과 M을 입력 받는다
    N, M = map(int, input().split())
    # 암호 코드를 입력받는다.
    barcode = [input()[:M] for _ in range(N)]

    # 16진수 코드를 2진수 코드로 변환
    binary = change_to_binary()
    # 2진수 코드를 10진수 코드로 변환
    decimal = change_to_decimal()
    # 10진수 코드에서 중복을 제거
    decimal_complete = list(set(decimal))

    # 10진수 코드 검증 결과 출력
    print('#{} {}'.format(tc, cal()))
