# SWEA 반례 모두 통과
# 실행시간 725ms

import sys
sys.stdin = open('input.txt')


# 금액을 계산하는 함수
def cal(price):
    # 결과를 0으로 초기화
    result = 0
    # 증가분을 1로 초기화
    inc = 1

    # 뒤에서부터 계산해야 하므로, price에서 역순으로 숫자를 꺼낸다.
    for idx in range(len(price) - 1, -1, -1):
        # inc를 10배씩 늘려가며 result에 숫자를 더한다.
        result += price[idx] * inc
        inc *= 10

    # 결과값 반환
    return result


# 교환을 하는 함수
# price : 금액을 담은 리스트
# cnt : 재귀 실행 횟수
# ans : 정답을 담은 리스트
def swap(price, cnt, ans):
    if cnt == chance:
        """
        종료 조건 : 재귀 실행 횟수(cnt)가 chance와 같아질 때
        """
        # price를 정답과 비교할 상금으로 계산
        compare = cal(price)
        # 상금이 정답보다 크면, 정답을 상금으로 바꿈
        if compare > ans[0]:
            ans[0] = compare
    else:
        """
        실행 조건 : 재귀 실행 횟수(cnt)가 아직 chance보다 작을 때
        """
        # 정답이 최대 금액이 아닐 경우에만 교환 실행
        # 교환을 통해 최대 금액을 받을 수 있다는 사실이 증명되었다면, 더 이상은 교환을 할 필요가 없기 때문!
        if ans[0] != max_price:
            # 인덱스 모음 indice에서 인덱스 쌍을 꺼낸다
            for index in indice:
                # 꺼낸 인덱스 쌍끼리 교환
                price[index[0]], price[index[1]] = price[index[1]], price[index[0]]
                # 교환한 이후의 price를 복사
                price_copy = price[:]
                # 현재 상태의 price가 동일한 깊이에서 나온 적이 있는지 체크
                # 나온 적이 없다면 check에 현재 price를 추가하고 다음 교환 실시
                if price_copy not in check[cnt]:
                    check[cnt].append(price_copy)
                    swap(price, cnt+1, ans)
                # price를 다시 원래대로 돌려놓는다
                price[index[0]], price[index[1]] = price[index[1]], price[index[0]]


# main
T = int(input())

for tc in range(1, T+1):
    # 금액(숫자판)과 기회 입력 방기
    price, chance = input().split()

    # 금액을 정수형 리스트로, 기회를 정수로 변환
    price = list(map(int, list(price)))
    chance = int(chance)
    # 중복을 체크할 이차원 리스트 check 생성
    check = [[] for _ in range(chance)]

    # 교환해야 할 인덱스 쌍을 담을 리스트 indice 생성
    indice = []
    # 서로 교환 가능한 모든 인덱스 쌍은 indice에 담는다
    for i in range(len(price) - 1):
        for j in range(i+1, len(price)):
            indice.append((i, j))

    # 받을 수 있는 최대 금액을 구한다
    # 최대 금액은 price의 숫자들이 역순으로 정렬된 경우이다
    sorted_price = sorted(price, reverse=True)
    max_price = cal(sorted_price)

    # 정답을 담을 리스트 ans 생성
    ans = [0]
    # 교환 실행
    swap(price, 0, ans)

    # 정답 출력
    print('#{} {}'.format(tc, ans[0]))
