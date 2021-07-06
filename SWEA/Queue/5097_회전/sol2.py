# 라이브강의 해설
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N : 숫자의 갯수, M : 이동할 횟수

    queue = input().split()

    for i in range(M):
        # tmp = queue.pop(0)
        # queue.append(tmp)

        queue.append(queue.pop(0))

    print('#{} {}'.format(tc, queue.pop(0)))