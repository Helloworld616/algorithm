# 숫자 비교로 푼 코드

import sys
sys.stdin = open('input.txt')

for num in range(1, 11):
    T = int(input())
    cnt = 0
    building = list(map(int, input().split()))
    for i in range(2, len(building)-2):
        if building[i] > building[i-2] and building[i] > building[i-1] and building[i] > building[i+1] and building[i] > building[i+2]:
            neighbors = [building[i-2], building[i-1], building[i+1], building[i+2]]
            highest = neighbors[0]
            for n_len in range(1, len(neighbors)):
                if neighbors[n_len] > highest:
                    highest = neighbors[n_len]
            cnt += building[i]-highest

    print('#{} {}'.format(num, cnt))