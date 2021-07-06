# 교수님 해설 2

import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    # 아파트 단지의 가로 길이
    length = int(input())
    buildings = list(map(int, input().split()))

    # 조망권 확보된 집
    total = 0

    idx = 2
    while idx < length-2: # for은 index 마음대로 조절 못 함!
        # 5개 집
        l1, l2, current, r1, r2 = [buildings[idx+n] for n in range(-2, 3)]

        sides = [l1, l2, r1, r2]

        highest = sides[0]
        for side in sides:
            if side > highest:
                highest = side
        # 확보!
        if current > highest:
            total += current - highest
            idx += 3 # 뒤 두 개 집은 어차피 view가 안 좋음
        else:
            idx += 1

    print('#{} {}'.format(tc, total))