import sys
sys.stdin = open('sample_input.txt')

T = int(input())
A = [i for i in range(1, 13)]

for tc in range(1, T+1):
    N, K = map(int, input().split())
    cnt = 0
    for i in range(1 << 12):
        total = 0
        check = 0
        answer = []
        for j in range(13):
            if i & (1 << j):
                total += A[j]
                answer.append(A[j])
                check += 1
        if total == K and check == N:
            cnt += 1
    print('#{} {}'.format(tc, cnt))