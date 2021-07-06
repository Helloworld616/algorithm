import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    pascal = [[1]+[0]*(N-1) for _ in range(N)]
    for i in range(1, N):
        for j in range(1, N):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            if pascal[i][j] != 0:
                print(pascal[i][j], end = ' ')
        print()
