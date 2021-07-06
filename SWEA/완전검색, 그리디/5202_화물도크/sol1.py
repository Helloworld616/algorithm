import sys
sys.stdin = open('sample_input.txt')


# 버블 정렬 함수
# 종료 시간을 기준으로 정렬
def bubble_sort(arr):
    for i in range(len(arr)-1, -1, -1):
        for j in range(i):
            if arr[j][1] > arr[j+1][1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# 이용할 수 있는 화물차의 최대 대수를 구하는 함수
def make_schedule():
    # 최대 대수가 이용하는 스케줄을 저장할 리스트 schedule 생성
    schedule = []
    # time에 저장된 (시작 시간, 종료 시간)을 꺼낸다.
    for part_time in time:
        # schedule이 비어 있을 경우 바로 추가
        if not len(schedule):
            schedule.append(part_time)
        # schedule이 비어 있지 않을 경우
        # 시작 시간이 현재 스케줄의 종료 시간보다 뒤일 경우에만 추가
        else:
            if part_time[0] >= schedule[-1][1]:
                schedule.append(part_time)

    # schedule의 길이 반환
    return len(schedule)


# main
T = int(input())

for tc in range(1, T+1):
    # 신청 대수 입력 받기
    N = int(input())

    # 각 화물차의 시작 시간과 종료 시간을 담을 리스트 time 생성
    time = []
    # 시작 시간과 종료 시간을 입력 받아 time에 추가
    for _ in range(N):
        s, e = map(int, input().split())
        time.append([s, e])

    # 종료 시간을 기준으로 버블 정렬 수행
    bubble_sort(time)

    # 정답 출력
    print(f'#{tc} {make_schedule()}')
