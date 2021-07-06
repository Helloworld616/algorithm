import sys
sys.stdin = open('sample_input.txt')


# 백트래킹 함수
# cnt : 이동 횟수
# row : 방문한 골프장의 행 좌표
# battery : 배터리 사용량을 누적시킬 리스트
# record : 지금까지 거쳐온 좌표를 기록하는 리스트
# result : 최종 이동거리들을 담을 결과 리스트
def move(cnt, row, battery, record, result):
    if cnt == N-1:
        """
        종료 조건 : 이동 횟수가 (N-1)과 같아질 때
        """
        # 도착지는 출발점으로 고정되어 있다
        # 도착지의 배터리 사용량을 battry에 더하고, battery의 총 합산 값을 result에 추가한다.
        result.append(sum(battery + [golf_course[row][0]]))
    else:
        """
        실행 조건 : 이동 횟수가 아직 (N-1)에 도달하지 못할 때
        """
        # 반복문으로 좌표를 하나씩 꺼낸다
        for i in range(N):
            # 첫 번째 탐색 조건 : 아직 방문하지 않은 좌표여야 한다.
            if i not in set(record):
                # battery에 배터리 사용량 누적
                battery.append(golf_course[row][i])

                # 두 번째 탐색 조건
                # 1. 결과 리스트에 아직 아무 값도 없어야 한다.
                # 2. 결과 리스트에 결과값이 하나라도 있을 경우, 결과값들의 최솟값보다 현재 배터리 사용량이 더 작아야 한다.
                if len(result) == 0 or (len(result) > 0 and sum(battery) < min(result)):
                    # 탐색 조건을 모두 통과했을 경우 다음 좌표 탐색
                    move(cnt+1, i, battery, record + [i], result)

                # battery를 다시 원래대로 되돌려놓는다
                battery.pop()


# main
T = int(input())

for tc in range(1, T+1):
    # 골프장의 크기, 골프장 입력 받기
    N = int(input())
    golf_course = [list(map(int, input().split())) for _ in range(N)]

    # 최종 이동거리들을 담을 결과 리스트 생성
    result = []
    # 백트래킹 시행
    move(0, 0, [], [0], result)

    # 최종 이동거리 중 최소값을 출력
    print('#{} {}'.format(tc, min(result)))
