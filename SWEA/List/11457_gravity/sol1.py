# 런타임 에러

import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(1, T+1):
    N = int(input())
    boxes = list(map(int, input().split()))
    room = []
    max_num = 0
    for box in boxes:
        room.append([1]*box + [0]*(N-box))
    for row in range(len(room)-2, -1, -1):
        for col in range(len(room[row])):
            cnt = 0
            for idx in range(row, len(room)-1):
                if room[idx][col] > room[idx+1][col]:
                    room[idx][col], room[idx+1][col] = room[idx+1][col], room[idx][col]
                    cnt += 1
            if cnt > max_num:
                max_num = cnt

    print("#{} {}".format(i, max_num))

