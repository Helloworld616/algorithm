import sys
sys.stdin = open('input.txt')

# 이진수를 십진수로 변경할 수 있는 정보를 담은 딕셔너리
change = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5,
          '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

# 암호 패턴을 찾는 함수
def find_password():
    # flag 변수를 False로 활용
    # 암호를 찾는 순간 True로 변해서, 필요한 연산이 수행되게 해 줌
    flag = False
    # 암호 초기화
    password = ''

    # 배열을 순회하면서 암호 탐색
    for i in range(N):
        # 모든 암호는 끝에 1이 존재한다는 공통점을 가짐
        # 이 특성을 이용하기 위해 배열의 한 줄을 역순으로 탐색
        for j in range(M-1, -1, -1):
            # 만약 글자가 1이라면 flag 변수를 True로 변경
            if matrix[i][j] == '1':
                flag = True
            # flag 변수가 True가 되는 순간 암호가 생성됨
            # 뒤에서부터 암호의 글자가 하나씩 붙여짐
            if flag:
                password = matrix[i][j] + password
            # 암호의 길이가 56이 되는 순간 반환
            if len(password) == 56:
                return password


# main
T = int(input())

for tc in range(1, T+1):
    # N, M과 전체 배열 입력 받기
    N, M = map(int, input().split())
    matrix = [input() for _ in range(N)]

    # 암호 패턴을 찾는다.
    password = find_password()

    # 암호 분절 결과를 담을 리스트 생성
    password_list = []
    # 암호를 7글자씩 분절하여 리스트에 담는다
    for i in range(0, len(password), 7):
        password_list.append(password[i:i+7])

    # 암호 변환 결과를 담을 리스트 생성
    change_list = []
    # 맨 처음에 선언한 딕셔너리 change를 활용해 이진수 암호를 십진수로 변경
    for number in password_list:
        change_list.append(change[number])

    # 유효성 여부를 체크할 변수 check와
    # 홀수 번째 숫자를 합산할 변수 odd를 생성하여 초기화
    check = 0
    odd = 0

    # change_list를 순회하여 점검
    # 인덱스가 0부터 시작하므로 짝수 인덱스가 홀수 번째, 홀수 인덱스가 짝수 번째 수이다!
    for i in range(len(change_list)):
        # 인덱스가 홀수일 경우 check에 숫자 합산
        if i % 2:
            check += change_list[i]
        # 인덱스가 짝수일 경우 odd에 숫자 합산
        else:
            odd += change_list[i]
    # odd를 3배한 값을 check에 합산
    check += odd * 3

    # check가 10으로 나누어 떨어지지 않으면 답에 0을 할당
    if check % 10:
        ans = 0
    # 나누어 떨어질 경우 change_list의 총합 결과를 할당
    else:
        ans = sum(change_list)

    # 결과(ans) 출력
    print('#{} {}'.format(tc, ans))
