import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    puzzle = [list(map(int, input().split()))+[0] for _ in range(N)]
    puzzle.append([0]*(N+1))

    ans = 0

    for i in range(N):
        cnt = 0
        # 벽을 한 칸 더 불렀기 때문에 증가
        for j in range(N+1):
            if puzzle[i][j]:
                cnt += 1
            else:
                if cnt == N:
                    ans += 1
                cnt = 0

        # 열우선순회
        for j in range(N+1):
            if puzzle[j][i]:
                cnt += 1
            else:
                if cnt == N:
                    ans += 1
                cnt = 0

    print("#{} {}".format(tc, ans))