import sys
sys.stdin = open('input.txt')


def power(N, M):
    if M == 1:
        return N
    return N * power(N, M-1)


for tc in range(1, 11):
    T = int(input())
    N, M = map(int, input().split())
    print('#{} {}'.format(tc, power(N, M)))

