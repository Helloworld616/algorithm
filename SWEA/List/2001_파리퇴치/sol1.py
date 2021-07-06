import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    array = []
    for i in range(N):
        flies = list(map(int, input().split()))
        array.append(flies)

    max_num = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for row in range(M):
                for col in range(M):
                    total += array[i + row][j + col]
            if total > max_num:
                max_num = total

    print('#{} {}'.format(tc, max_num))