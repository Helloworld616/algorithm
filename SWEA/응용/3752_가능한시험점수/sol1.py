# 문자열의 특성을 이용한 방법
# 시간초과

"""
문자열로 덧셈을 수행하면 더한 숫자들이 그대로 나열된다는 점을 이용한 방법입니다.

예를 들어 문자 '2'와 '3'을 더하면 '23'이 되어서, 이미 2와 3이 더해졌다는 사실을 알 수가 있습니다.
이 점을 통해 중복을 피한 연산을 수행하려고 했습니다...만 시간이 오래 걸려서 시간초과가 났습니다 -_-;;;
"""
import sys
sys.stdin = open('sample_input.txt')


T = int(input())

for tc in range(1, T+1):
    # 문제의 갯수와 배점 입력 받기
    N = int(input())
    scores = input().split()
    # 배점에서 중복을 제거한 뒤 리스트로 변환
    numbers = list(set(scores))

    # 배점에서 점수를 하나씩 꺼낸다
    for score in scores:
        # 배점이 하나 나올 때마다 numbers에서 숫자들을 모두 꺼내 연산을 수행한다.
        for number in numbers:
            # 배점과 점수를 합친 뒤 (문자열 연산)
            # 리스트로 만들고 정렬한 후 문자열로 변환 (join 연산)
            new_number = ''.join(sorted(list(score + number)))
            # 만약 number안의 점수 갯수가 배점 안의 점수 갯수보다 작고
            # 기존의 점수 리스트 안에 현재의 연산 결과가 없을 경우
            if number.count(score) < scores.count(score) and new_number not in set(numbers):
                # numbers에 연산 결과 추가
                numbers.append(new_number)

    # 최종 연산 결과를 담을 리스트 result 생성
    result = []
    # numbers 안의 number들이 가지고 있는 숫자를 전부 더하여 result에 넣는다.
    for number in numbers:
        result.append(sum(list(map(int, list(number)))))

    # result에서 중복을 제거한 뒤, result의 길이에 1을 더한 결과를 출력한다.
    # 길이에 1을 더하는 이유는 0까지 포함해야 하기 때문!
    print('#{} {}'.format(tc, len(set(result))+1))

