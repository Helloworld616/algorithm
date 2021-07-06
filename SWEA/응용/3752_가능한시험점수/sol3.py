# Dynamic Programming 1
# 시간 초과

"""
첫 번째 DP 풀이 시도.

Memoization을 활용한 방법입니다. 점수를 계산 할 때마다 기록을 합니다.
그리고 기록을 한 점수에 계산하지 않은 배점들을 계속 더해가면서 최종 결과를 산출합니다.

하지만 이 방법을 사용하려면 중간중간 기록한 공간에 중복이 있는지 없는지 점검을 해야하는데
이 부분에서 시간 초과가 났습니다.

점검을 하지 않으면 Runtime Error가 납니다.
"""
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    # 문제의 갯수와 배점 입력 받기
    N = int(input())
    scores = list(map(int, input().split()))

    # 결과를 담을 리스트 result 생성
    # Base Case는 0
    result = [0]

    # 배점 리스트에서 배점을 하나씩 꺼낸다
    for score in scores:
        # result의 길이를 미리 저장한다.
        # 무한루프를 방지하기 위함이다!
        length = len(result)
        # length만큼 반복문 실행
        for i in range(length):
            # 기존 점수와 배점의 합산 결과가 아직 result에 없을 경우 추가
            # 이 조건문이 없으면 Runtime Error 발생!
            if result[i]+score not in set(result):
                result.append(result[i]+score)

    # result의 길이 출력
    print('#{} {}'.format(tc, len(result)))

