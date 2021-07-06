import sys
sys.stdin = open('sample_input.txt')


def attach(cnt):
    if cnt == 1:
        return 1
    if cnt == 2:
        return 3
    return 2 * attach(cnt - 2) + attach(cnt - 1)


T = int(input())


for tc in range(1, T+1):
    N = int(input())
    cnt = N // 10
    print("#{} {}".format(tc, attach(cnt)))