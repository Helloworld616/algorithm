# 오답

import sys
sys.stdin = open('sample_input.txt')


def move(idx, change, distance):
    global ans

    if change < ans:
        if distance >= N:
            ans = change
        else:
            for i in range(idx + 1, distance + 1):
                move(i, change + 1, distance + battery[i])


# main
for tc in range(1, int(input())+1):
    battery = list(map(int, input().split()))
    N = battery[0]

    ans = N-1

    move(1, 0, 1 + battery[1])

    print('#{} {}'.format(tc, ans))
