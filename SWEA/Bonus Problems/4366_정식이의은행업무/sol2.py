import sys
sys.stdin = open('sample_input.txt')


# 자릿수를 바꿔가며 경우의 수를 도출하는 함수
# idx : 원본 숫자에서 자릿수를 바꿀 인덱스
# numbers : 자릿수에 들어갈 수 있는 숫자들
# origin : 원본 숫자
# result : 모든 경우의 수를 담는 리스트
def change(idx, numbers, origin, result):
    # idx가 원본 숫자 길이보다 작을 경우 실행
    if idx < len(origin):
        # 원본 숫자의 원래 자릿수를 따로 저장
        origin_num = origin[idx]

        # numbers에서 숫자들을 하나씩 꺼내서,
        # 원본 숫자와 다를 경우 idx 위치에 집어넣는다.
        # 집어넣은 후의 결과값을 result에 추가
        for number in numbers:
            if number == origin_num:
                continue
            origin[idx] = number
            value = ''.join(origin)
            result.append(value)

        # 원본 숫자의 원래대로 돌려놓는다.
        origin[idx] = origin_num
        # 다음 자릿수로 넘어간다.
        change(idx+1, numbers, origin, result)


# 경우의 수를 key로, 경우의 수를 10진수로 바꾼 결과를 value로 가지는 딕셔너리 생성 함수
# numbers : 경우의 수들이 들어있는 리스트
# delta : n진수를 10진수로 변환하기 위한 숫자 (2진수일 경우 delta=2, 3진수일 경우 delta=3)
def make_dict(numbers, delta):
    # 결과값을 담을 딕셔너리 생성
    result = dict()

    # 경우의 수를 하나씩 꺼낸다.
    for number in numbers:
        # 경우의 수를 리스트로 변환
        number_list = list(number)
        # 10진수 변환값을 0으로 초기화
        decimal = 0
        # 증가분을 1로 초기화
        inc = 1

        # 'n진수 -> 10진수' 변환
        # number_list의 뒤에서부터 계산 (앞자리로 갈 수록 증가분이 더 커지므로!)
        for i in range(len(number_list)-1, -1, -1):
            decimal += int(number[i]) * inc  
            inc *= delta

        # result에 key와 value 추가
        result[number] = decimal

    # 최종 딕셔너리 반환
    return result


# 2진수 사전과 3진수 사전에서 공통으로 나오는 수를 찾아 반환하는 함수
# binary_dict : 2진수 사전
# ternary_dict : 3진수 사전
def cal(binary_dict, ternary_dict):
    # 각 사전을 value 값을 이중루프로 하나씩 비교하여
    # 같을 경우 그 값을 바로 반환한다.
    for b_value in binary_dict.values():
        for t_value in ternary_dict.values():
            if b_value == t_value:
                return b_value


# main
for tc in range(1, int(input())+1):
    # 2진수, 3진수를 문자열 리스트로 입력받기
    binary = list(input())
    ternary = list(input())

    # 2진수에서 나올 수 있는 경우의 수를 담는 리스트 생성
    binary_result = []
    # 경우의 수 도출
    change(0, ['0', '1'], binary, binary_result)
    # 경우의 수를 key로, 경우의 수를 10진수로 바꾼 결과를 value로 가지는 딕셔너리 생성
    binary_dict = make_dict(binary_result, 2)

    # 3진수에서 나올 수 있는 경우의 수를 담는 리스트 생성
    ternary_result = []
    # 경우의 수 도출
    change(0, ['0', '1', '2'], ternary, ternary_result)
    # 경우의 수를 key로, 경우의 수를 10진수로 바꾼 결과를 value로 가지는 딕셔너리 생성
    ternary_dict = make_dict(ternary_result, 3)

    # binary_dict와 tenary_dict에서 공통으로 나오는 수를 찾아서 출력
    print('#{} {}'.format(tc, cal(binary_dict, ternary_dict)))
