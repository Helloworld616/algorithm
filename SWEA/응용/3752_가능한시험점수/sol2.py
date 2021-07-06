# 백트래킹
# 시간초과

"""
백트래킹을 이용한 방법입니다. 탐색을 통해 합산 가능한 숫자들의 조합을 구해서 마지막에는 덧셈을 합니다.
마지막에는 이렇게해서 구한 덧셈 결과에서 중복을 제거한 뒤 정답을 도출합니다.
하지만 이것도 시간초과가 났습니다...
"""
import sys
sys.stdin = open('sample_input.txt')


# 백트래킹 함수
# idx : 반복문의 시작점이 될 인덱스
# temp : 연산에 필요한 숫자들을 담을 리스트
# result : 연산 결과를 담을 리스트
def cal(idx, temp, result):
    if idx == len(scores)-1:
        """
        종료 조건 : 인덱스가 (scores의 길이 - 1)이 되었을 때
        """
        temp.append(scores[idx])
        result.append(sum(temp))
        temp.pop()
    else:
        """
        실행 조건 : 인덱스가 아직 (scores의 길이 - 1)이 되지 않았을 때
        """
        # 인덱스부터 scores의 길이까지 반복문 실행
        for i in range(idx, len(scores)):
            # temp의 sum과 점수를 더해서 중간 합산 결과 total을 구한다.
            total = sum(temp) + scores[i]
            """
            백트래킹 조건 : total이 아직 결과 리스트 result에 없을 경우에만 다음 탐색 실행
            """
            if total not in set(result):
                # temp에 점수를 추가하고
                temp.append(scores[i])
                # result에 total을 추가한 뒤
                result.append(total)
                # 다음 탐색 실행
                cal(i+1, temp, result)
                # 탐색 실행 후에는 temp를 다시 원래대로 되돌려놓는다
                temp.pop()


# main
T = int(input())

for tc in range(1, T+1):
    # 문제의 갯수와 배점 입력 받기
    N = int(input())
    scores = list(map(int, input().split()))
    # 배점 리스트 scores 정렬
    scores.sort()

    # 최종 결과를 담을 리스트 result 생성
    result = []
    # 백트래킹 시행
    cal(0, [], result)

    # result에서 중복을 제거한 뒤, result의 길이에 1을 더한 결과를 출력한다.
    # 길이에 1을 더하는 이유는 0까지 포함해야 하기 때문!
    print('#{} {}'.format(tc, len(set(result))+1))
