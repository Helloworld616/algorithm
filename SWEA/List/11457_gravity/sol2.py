# import sys
# sys.stdin = open('input.txt')

T = int(input())

for i in range(1, T+1):
    N = int(input())
    room = list(map(int, input().split()))
    max_num = 0
    for j in range(len(room)-2, -1, -1):
        cnt = 0
        for idx in range(j, len(room)-1):
            if room[idx] > room[idx+1]:
                temp = room[idx] - room[idx+1]
                room[idx+1] += temp
                room[idx] -= temp
                cnt += 1
        if max_num < cnt:
            max_num = cnt
    print("#{} {}".format(i, max_num))
