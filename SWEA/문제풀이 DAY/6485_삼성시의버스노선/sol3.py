import sys
sys.stdin = open('s_input.txt')

T = int(input())
for tc in range(1, T+1):
    # input 받기
    N = int(input()) # 버스(노선) 개수

    lane = [0] * 5001 # 0~5000
    for idx in range(N):
        first_stop, last_stop = tuple(map(int, input().split()))
        for stop in range(first_stop, last_stop+1):
            lane[stop] += 1

    P = int(input())
    stop_list = [] # 검증할 정류장들
    for idx in range(P):
        my_stop = int(input())
        stop_list += [my_stop]

    # result = ''
    # for idx in range(len(stop_list)):
    #     result += str(lane[stop_list[idx]])
    # print(result)
    # result = ' '.join(result)
    # print(type(result))
    #
    # print('#{} {}'.format(tc, result))

    result = []
    for idx in range(len(stop_list)):
        result += [lane[stop_list[idx]]]
    result = ' '.join(map(str, result))
    print(type(result))

    print('#{} {}'.format(tc, result))