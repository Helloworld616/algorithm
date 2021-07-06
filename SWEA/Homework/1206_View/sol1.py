# 2차원 배열로 푼 코드

import sys
sys.stdin = open('input.txt')

for num in range(1, 11):
    T = int(input())
    area = []
    cnt = 0
    buildings = list(map(int, input().split()))
    for building in buildings:
        area.append([1]*building + [0]*(255-building))
    for i in range(2, T-2):
        for j in range(255):
            if area[i][j] and not area[i-2][j] and not area[i-1][j] and not area[i+1][j] and not area[i+2][j]:
                cnt += 1
    print('#{} {}'.format(num, cnt))

