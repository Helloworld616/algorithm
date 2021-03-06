# import sys
# sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    cards = list(map(int, list(input())))
    counter = [0] * 10
    # 2가 되면 성공
    is_babygin = 0

    for card in cards:
        counter[card] += 1

    idx = 0
    while idx < len(counter):
        # triplet 검증
        if counter[idx] >= 3:
            is_babygin += 1
            counter[idx] -= 3
            # 추가 triplet 여부 검사
            if counter[idx] >= 3:
                idx -= 1
        # run 검증
        if idx < 8:
            if counter[idx] != 0 and counter[idx+1] != 0 and counter[idx+2] != 0:
                is_babygin += 1
                counter[idx] -= 1
                counter[idx+1] -= 1
                counter[idx+2] -= 1
            # 추가 run 여부 검사
            if counter[idx] > 0 and counter[idx+1] > 0 and counter[idx+2] > 0:
                idx -= 1
        idx += 1

    if is_babygin == 2:
        result = 1
    else:
        result = 0

    print('#{} {}'.format(tc, result))