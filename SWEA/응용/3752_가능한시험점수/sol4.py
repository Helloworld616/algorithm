# Dynamic Programming 2
# Pass

"""
두 번째 DP 풀이 시도.

첫 번쨰 DP에서 중복 체크를 할 때 시간 초과가 나는 것을 보고 이것을 어떻게 처리할 지 고민했습니다.
그리고 생각 끝에 처음부터 중복을 없애주는 방법을 생각해냈습니다.

배점에서 최댓값이 되는 점수는 모든 배점을 합한 값입니다.
따라서 산출 가능한 점수의 범위는 "0 ~ 모든 배점의 합"이 됩니다.

그렇다면
1. "모든 배점의 합" 만큼의 크기를 가진 리스트를 만든 뒤
2. 연산 도출 여부를 모두 False로 초기화하고
3. 연산을 통해 도출될 때마다 True로 처리하면 되지 않을까?
라는 생각이 들었습니다. 그리고 이렇게 했더니 드디어 Pass를 받았습니다.

연산 과정은 첫 번째 DP와 거의 비슷합니다만, 이번에는 합산을 Memoization 리스트의 끝에서부터 해야 합니다.
그렇게 하지 않으면 "같은 연산 단계에서 True로 표시한 수"도 연산에 포함시켜서 제대로 된 답이 나오지 않기 때문입니다.

"""

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    # 문제의 갯수와 배점 입력 받기
    N = int(input())
    scores = list(map(int, input().split()))

    # Dynamic Programming 수행 리스트 생성
    # 크기는 배점의 합. 원소는 모두 False로 초기화
    dp = [False for _ in range(sum(scores)+1)]
    # Base Case가 되는 0은 True로 변경
    dp[0] = True

    # 연산 수행
    # 배점에서 점수를 하나씩 꺼낸다
    for score in scores:
        # dp 리스트의 끝에서부터 연산 수행
        # 끝에서부터 수행하는 이유는 잘못된 연산 누적을 피하기 위함이다!
        for i in range(len(dp)-1, -1, -1):
            # 숫자의 dp 값이 True일 경우 (= 과거에 연산을 실행했을 경우)
            if dp[i]:
                # 그 숫자에 배점을 더한 합산 결과의 dp 값을 True로 변경해준다.
                dp[i + score] = True

    # dp 리스트에 존재하는 True의 갯수를 출력
    print('#{} {}'.format(tc, dp.count(True)))
