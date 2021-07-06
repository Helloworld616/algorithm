import sys
sys.stdin = open("input.txt")


def solution(progresses, speeds):
    answer = []

    # progresses가 있는 한 계속 작업 시행
    while progresses:
        # 하루 치 작업량 만큼 progresses 안의 작업 진도를 증가시킴
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        # 끝난 작업이 있는지 검사
        # 안 끝난 작업이 나올 때까지 검사한다!
        cnt = 0
        while len(progresses) and progresses[0] >= 100:
            # 끝난 작업이 있으면 progresses와 speeds 안의 작업 내용을 빼내고
            # 배로 횟수 1 증가시킴
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1

        # 작업이 하나라도 있을 경우 answer에 추가
        if cnt > 0:
            answer.append(cnt)

    # 정답 반환
    return answer


# main
T = int(input())

for tc in range(1, T+1):
    progresses = list(map(int, input().split()))
    speeds = list(map(int, input().split()))
    
    print("#{} {}".format(tc, solution(progresses, speeds)))

