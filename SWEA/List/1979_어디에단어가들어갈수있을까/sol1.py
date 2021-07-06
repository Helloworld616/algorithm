import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    edge1 = [0] * (N + 2)
    edge2 = [0] * (N + 2)
    puzzle = [edge1]
    for i in range(N):
        space = list(map(int, input().split()))
        space.insert(0, 0)
        space.append(0)
        puzzle.append(space)
    puzzle.append(edge2)

    answer = 0
    for i in range(N+2):
        cnt = 0
        for j in range(N+2):
            if puzzle[i][j] == 1:
                cnt += 1
            else:
                if cnt == K:
                    answer += 1
                cnt = 0

    for i in range(N+2):
        cnt = 0
        for j in range(N+2):
            if puzzle[j][i] == 1:
                cnt += 1
            else:
                if cnt == K:
                    answer += 1
                cnt = 0

    print('#{} {}'.format(tc, answer))
