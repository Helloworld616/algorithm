# 시간 초과
import sys
sys.stdin = open('sample_input.txt')


def hamburger(val, cal, total_c, total_v, result, visit, L):
    for idx in range(len(val)):
        if not visit[idx]:
            total_c += cal[idx]
            if total_c > L:
                result.append(total_v)
            elif total_c == L:
                result.append(total_v + val[idx])
            else:
                total_v += val[idx]
                visit[idx] = True
                hamburger(val, cal, total_c, total_v, result, visit, L)
                total_v -= val[idx]
                visit[idx] = False
            total_c -= cal[idx]
        if False not in set(visit):
          result.append(total_v)


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
    visit = [False] * N
    hamburger(val, cal, 0, 0, result, visit, L)
    print('#{} {}'.format(tc, max(result)))