# Brute Force

"""
이 코드는 강의자료에서 안내하는 완전탐색 알고리즘을 충실히 따라서 구현한 결과입니다.

6개의 카드에서 나올 수 있는 조합을 전부 구하는데,
하나의 조합이 나올 때마다 왼쪽 3개의 카드와 오른쪽 3개의 카드를 검사해서 baby-gin 여부를 판단합니다.

그리고 그 결과(0 혹은 1)를 집합에 저장해서 집합의 최댓값을 출력합니다.

"""

import sys
sys.stdin = open('input.txt')


# 완전탐색 함수
# case : 조합 케이스를 담는 리스트
# record : 이미 탐색한 인덱스를 기록하는 집합
# result : baby-gin 여부를 기록하는 집합
def baby_gin(case, record, result):
    if len(case) == 6:
        """
        종료조건 : 조합 케이스의 길이가 6이 되었을 경우
        """
        # 6개의 카드를 왼쪽 1, 2, 3번 카드와 오른쪽 4, 5, 6번 카드로 나누어서 비교한다.

        # 인덱스는 0부터 시작하므로 실제 카드의 순서 번호보다 1 작다.
        # 3, 2번쨰 카드 간의 차이와 6, 5번쨰 카드 간의 차이를 각각 구한다.
        left_diff = case[2] - case[1]
        right_diff = case[5] - case[4]

        # 만약 두 차이가 모두 0이나 1일 경우
        if 0 <= left_diff <= 1 and 0 <= right_diff <= 1:
            # 나머지 카드의 차이와도 일치하는지 검사한다.
            # 일치할 경우 baby-gin이므로 result에 1 추가, 아닐 경우 0 추가
            if case[1] - case[0] == left_diff and case[4] - case[3] == right_diff:
                result.add(1)
            else:
                result.add(0)
        # 만약 두 차이 중 하나라도 0이나 1이 아닐 경우에는 result에 0추가
        else:
            result.add(0)
    else:
        """
        실행조건 : 조합 케이스의 길이가 아직 6이 되지 않았을 경우
        """
        for i in range(6):
            # 지금까지의 탐색 중 인덱스 i를 거치지 않았다면
            if i not in record:
                # 조합 케이스에 i번째 카드 추가
                case.append(cards[i])
                # 탐색 기록에 인덱스 i 추가
                record.add(i)
                # 다음 탐색 진행
                baby_gin(case, record, result)
                # 조합 케이스와 탐색 기록을 원래대로 돌려놓는다.
                case.pop()
                record.discard(i)


# main
for tc in range(1, int(input())+1):
    # 6개의 카드를 리스트로 입력 받기
    cards = list(map(int, list(input())))
    # 결과를 담을 집합 result를 생성
    result = set()
    # 완전탐색 실행
    baby_gin([], set(), result)
    # 결과 출력
    print('#{} {}'.format(tc, max(result)))
