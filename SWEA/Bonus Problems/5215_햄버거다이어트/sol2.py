import sys
sys.stdin = open('sample_input.txt')


def hamburger(val, cal, start, total_c, total_v, result, N, L):
    if start == N-1 and total_c <= L:
        result.append(total_v)
    else:
        for idx in range(start + 1, N):
            if total_c + cal[idx] > L:
                result.append(total_v)
            elif total_c + cal[idx] == L:
                result.append(total_v + val[idx])
            else:
                hamburger(val, cal, idx, total_c + cal[idx], total_v + val[idx], result, N, L)


T = int(input())

for tc in range(1, T+1):
    N, L = map(int, input().split())
    val = []
    cal = []

    for _ in range(N):
        v, c = map(int, input().split())
        val.append(v)
        cal.append(c)

    result = []
    for idx in range(N):
        hamburger(val, cal, idx, cal[idx], val[idx], result, N, L)

    print('#{} {}'.format(tc, max(result)))