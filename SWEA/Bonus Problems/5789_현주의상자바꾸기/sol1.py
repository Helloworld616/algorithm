import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    box = [0] * (N+1)
    i = 0
    for cnt in range(Q):
        L, R = map(int, input().split())
        i += 1
        for idx in range(L, R+1):
            box[idx] = i
    print('#{}'.format(tc), end = ' ')
    for idx in range(1, N+1):
        if idx==N:
            print(box[idx])
        else:
            print(box[idx], end = ' ')


