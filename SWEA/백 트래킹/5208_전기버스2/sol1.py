# 오답

import sys
sys.stdin = open('sample_input.txt')


def move(idx, change, possible):
    global ans

    if change < ans:
        new_change = change + 1
        new_possible = possible + battery[idx]
        if new_possible >= N:
            ans = new_change
        else:
            move(idx + 1, new_change, new_possible)
            move(idx + battery[idx], new_change, new_possible)


# main
for tc in range(1, int(input())+1):
    battery = list(map(int, input().split())) + [0]
    N = battery[0]

    ans = N-1
    possible = battery[1]
    change = 0

    move(2, change, possible)
    move(1 + battery[1], change, possible)

    print('#{} {}'.format(tc, ans))
