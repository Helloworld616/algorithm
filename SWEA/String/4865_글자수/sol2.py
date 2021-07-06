import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    # 키 = 문자, value = 카운트한 수
    my_dict = {}

    # str1의 문자를 가진 딕셔너리 생성
    for key in set(str1):
        my_dict[key] = 0

    for key in str2:
        if key in my_dict:
            my_dict[key] += 1

    ans = 0

    for i in my_dict.values():
        if ans < i:
            ans = i
    print('#{} {}'.format(tc, ans))