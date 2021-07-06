import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int, list(input()))) for _ in range(N)]

    start = N // 2 + 1
    end = N // 2
    total = 0

    for i in range(N):
        if i > N // 2:
            start += 1
            end -= 1
        else:
            start -= 1
            end += 1
        for j in range(start, end):
            total += farm[i][j]

    print('#{} {}'.format(tc, total))




