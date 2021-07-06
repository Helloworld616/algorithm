import sys
sys.stdin = open('sample_input.txt')


# 백트래킹 함수
# idx : 정류장 위치 (배터리 용량 리스트의 인덱스)
# change : 교환 횟수
def move(idx, change):
    global ans

    # 교환 횟수가 정답보다 작을 경우에만 백트래킹 실행
    if change < ans:
        # 도착지에 도달하는 순간, 교환 횟수를 바로 change에 저장
        # 교환 횟수가 정답보다 작은 상태이므로, 자동으로 최소값 갱신이 됨!
        if idx >= N:
            ans = change
        # 아직 도착지에 도착하지 못했을 경우,
        # '바로 다음 위치 ~ 도착할 수 있는 최장 거리'로 갈 경우의 백트래킹을 실시
        else:
            for i in range(1, battery[idx] + 1):
                move(idx+i, change + 1)


# main
for tc in range(1, int(input())+1):
    # 배터리 용량 입력 받기
    battery = list(map(int, input().split()))

    # 정류장의 수와 최대 교환 가능 횟수를 변수에 저잗
    N = battery[0]
    ans = N-1

    # 백트래킹 실시
    move(1, 0)

    # 정답 출력
    print('#{} {}'.format(tc, ans-1))
