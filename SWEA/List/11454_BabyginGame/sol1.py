# Greedy

"""
Greedy Algorithm은 매 단계에서, 가장 좋아 보이는 것을 빠르게 선택합니다.

이 코드에서 알고리즘이 선호하는 조건(검사를 하고 싶은 조건)은,
"연속된 3개의 숫자들의 갯수가 1 이상"이라는 것입니다.

run이 되는 조건이 "3장의 카드가 연속적인 번호를 갖는 것"이기 때문에,
연속된 3개의 숫자가 1:1:1 관계를 맺는지 검사해야 하기 때문이지요.
(이 코드에서는 전처리를 통해 triplet 검사는 스킵해도 무방하도록 처리했습니다.)

연속되는 숫자들이 서로 짝이 이루는지 검사한 다음, 그 여부에 따라 baby-gin인지 아닌지 판단합니다.

"""
import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(1, T+1):
    # 6개의 카드를 리스트로 입력 받기
    cards = list(map(int, list(input())))
    # 인덱스가 0부터 9까지 있는 counter 생성
    counter = [0]*10

    # 카드를 하나씩 꺼내서
    # 카운터에서 카드와 일치하는 인덱스를 1 증가시킨다. (= 해당 카드의 갯수를 1 증가시킴)
    for card in cards:
        counter[card] += 1

    # triplet 검사를 스킵하기 위한 전처리
    # counter의 모든 수를 3을 나눈 나머지로 바꾸어준다.
    # 이렇게 하면 triplet에 해당하는 수의 counter 값이 0이 되어 triplet 검사를 하지 않아도 된다!
    for idx in range(len(counter)):
        counter[idx] %= 3

    # run 검사 시작
    # counter의 인덱스를 1로 초기화
    idx = 1
    # 반복문 실행. Greedy 가동.
    while idx < len(counter)-1:
        # 연속되는 3개의 수가 모두 1개 이상의 값을 가질 경우, 모두 1을 빼준다.
        if counter[idx-1] >= 1 and counter[idx] >= 1 and counter[idx+1] >= 1:
            counter[idx-1] -= 1
            counter[idx] -= 1
            counter[idx+1] -= 1
        # 이 과정에서 하나라도 0이 될 경우, 다음 인덱스로 이동한다.
        if counter[idx-1] == 0 or counter[idx] == 0 or counter[idx+1] == 0:
            idx += 1

    # 모든 검사가 끝난 후, 카운터가 모두 0으로만 이루어져 있을 경우 baby-gin이다.
    if counter.count(0) == 10:
        print('#{} {}'.format(i, 1))
    # 0이 아닌 수가 하나라도 있을 경우 baby-gin이 아니다.
    else:
        print('#{} {}'.format(i, 0))
