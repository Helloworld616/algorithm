# Pass

import sys
sys.stdin = open('sample_input.txt')


# babygin 여부를 판별하는 함수
def is_babygin(player):
    # 카드가 0부터 9까지 있으므로
    # 0부터 9까지의 인덱스를 가진 counter 생성
    counter = [0] * 10

    # 1. triplet 검사
    # 플레이어의 카드들을 차례차례 확인
    for card in player:
        # 카운터에 카드의 개수를 하나씩 추가하다가
        counter[card] += 1
        # 개수가 3이 되는 순간 triplet을 확정짓고 승리 반환
        if counter[card] == 3:
            return True

    # 2. run 검사
    # 플레이어의 카드들을 3개씩 확인
    idx = 1
    while idx < len(counter) - 1:
        # 연속된 3개의 카드가 모두 1개 이상 씩 있을 경우
        # run을 확정 짓고 승리 반환
        if counter[idx - 1] >= 1 and counter[idx] >= 1 and counter[idx + 1] >= 1:
                return True
        # 검사 후 idx 1 증가
        idx += 1

    # triplet도, run도 아닐 경우 승리하지 않았음을 반환
    return False


# 승부 결과를 반환하는 함수
def fight(cards):
    # 각 플레이어의 카드를 담을 리스트 생성
    player1 = []
    player2 = []

    # 승부 시작
    for i in range(len(cards)):
        # 인덱스가 홀수일 때 (= 후공일 때)
        if i % 2:
            # player2가 카드를 뽑는다.
            player2.append(cards[i])
            # 3개 이상을 뽑은 상태에서 babygin이 성립하면 player2 승리
            if len(player2) >= 3 and is_babygin(player2):
                return 2
        # 인덱스가 짝수일 때 (= 선공일 때)
        else:
            # player1가 카드를 뽑는다.
            player1.append(cards[i])
            # 3개 이상을 뽑은 상태에서 babygin이 성립하면 player1 승리
            if len(player1) >= 3 and is_babygin(player1):
                return 1

    # 승부 결과가 나오지 않았다면 무승부(0) 반환
    return 0


# main
T = int(input())

for tc in range(1, T+1):
    # 카드를 리스트로 입력 받기
    cards = list(map(int, input().split()))
    # 승부 결과 출력하기
    print('#{} {}'.format(tc, fight(cards)))
