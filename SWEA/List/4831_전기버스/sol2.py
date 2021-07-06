# 라이브강의 해설 1

T = int(input())

for tc in range(1, T+1):
    # K : 이동할 수 있는 거리
    # N : 마지막 종점의 위치
    # M : 충전소의 개수
    K, N, M = map(int, input().split())

    charge = list(map(int, input().split()))

    bus_stop = [0] * (N+1)

    # 충전소를 표시하자!
    # for i in range(M):
    #     bus_stop[[charge[i]]] = 1

    for i in charge:
        bus_stop[i] = 1
    
    bus = 0 # 버스 위치
    ans = 0 # 충전 회수

    while True:
        # 버스가 이동할 수 있는 만큼 이동을 하자
        bus += K
        if bus >= N : break # 종점에 도착하거나 종점 지나 더 나아간 경우

        for i in range(bus, bus-K, -1):
            # if bus_stop[i] == 1:
            if bus_stop[i]:
                ans += 1
                bus = i
                break

        else:
            ans = 0
            break

    print('#{} {}'.format(tc, ans))