import sys
sys.stdin = open('sample_input.txt')


T = int(input())


for tc in range(1, T+1):
    N, M = map(int, input().split())
    flag = [list(input())  for i in range(N)]
    candidate = []
    total = 0

    for color in flag[0]:
        if color != 'W':
            total += 1

    for color in flag[len(flag)-1]:
        if color != 'R':
            total += 1

    for i in range(1, len(flag)-1):
        cnt = 0
        b_idx = i

        for color in flag[b_idx]:
            if color != 'B':
                cnt += 1

        w = []
        b = []
        candi = []
        for w_idx in range(1, b_idx):
            w_cnt = 0
            b_cnt = 0
            for color in flag[w_idx]:
                if color != 'W':
                    w_cnt += 1
                if color != 'B':
                    b_cnt += 1
            w.append(w_cnt)
            b.append(b_cnt)

        for j in range(len(w)+1):
            candi.append(sum(w[0:j]) + sum(b[j:len(b)]))
        if len(candi) > 0:
            cnt += min(candi)

        b = []
        r = []
        candi = []
        for r_idx in range(b_idx+1, len(flag)-1):
            b_cnt = 0
            r_cnt = 0
            for color in flag[r_idx]:
                if color != 'R':
                    r_cnt += 1
                if color != 'B':
                    b_cnt += 1
            r.append(r_cnt)
            b.append(b_cnt)

        for j in range(len(b)+1):
            candi.append(sum(b[0:j]) + sum(r[j:len(b)]))
        if len(candi) > 0:
            cnt += min(candi)

        candidate.append(cnt)

    print('#{} {}'.format(tc, total + min(candidate)))