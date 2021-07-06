# 교수님 해설

import sys
sys.stdin = open('input.txt')


def perm(idx, percentage):
    global N, maximum
    if idx == N:
        maximum = percentage
    else:
        for changer in range(idx, N):
            schedules[idx], schedules[changer] = schedules[changer], schedules[idx]
            # 지금까지의 일이 성공할 확률
            current_percentage = percentage * workers[idx][schedules[idx]]
            # 전체 최고 확률보다 지금까지의 성공 확률이 크다면, 진행 시켜
            if current_percentage > maximum:
                perm(idx+1, current_percentage)
            schedules[idx], schedules[changer] = schedules[changer], schedules[idx]


for tc in range(1, int(input()) + 1):
    # 사람의 수
    N = int(input())
    workers = [list(map(lambda x: int(x) / 100, input().split())) for _ in range(N)]
    schedules = [i for i in range(N)]
    maximum = 0
    perm(0, 1)
    print('#%d %.6f' % (tc, round(maximum * 100, 6)))
