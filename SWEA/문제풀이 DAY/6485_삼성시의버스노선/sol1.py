import sys
sys.stdin = open('s_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    bus_map = []
    answer = []
    for i in range(N):
        A, B = map(int, input().split())
        bus_road = []
        for num in range(A, B+1):
            bus_road.append(num)
        bus_map.append(bus_road)
    P = int(input())
    for j in range(P):
        C = int(input())
        cnt = 0
        for bus_road in bus_map:
            if C in bus_road:
                cnt += 1
        answer.append(cnt)

    print('#{}'.format(tc), end = ' ')
    for idx in range(len(answer)):
        if idx == len(answer)-1:
            print(answer[idx])
        else:
            print(answer[idx], end = ' ')

